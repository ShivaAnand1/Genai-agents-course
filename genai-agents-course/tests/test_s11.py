"""Session 11 checkpoint. Run with:  uv run pytest tests/test_s11.py
Offline tests check structure and parsing; live tests (skipped with no key) check real calls."""
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "module01"))
from providers_utils import (CLASSIFIER_SYSTEM, classify_ticket, gemini_client,  # noqa: E402
                             groq_client, ollama_client)
from tickets_data import ALL_TICKETS, BORDERLINE_TICKETS, CLEAR_TICKETS  # noqa: E402

HAS_GROQ = bool(os.getenv("API_KEY")) and "paste_your" not in os.getenv("API_KEY", "")
HAS_GEMINI = bool(os.getenv("GEMINI_API_KEY")) and "paste_your" not in os.getenv("GEMINI_API_KEY", "")


def test_ticket_data_has_clear_and_borderline_cases():
    assert len(CLEAR_TICKETS) >= 3
    assert len(BORDERLINE_TICKETS) >= 3
    ids = [t[0] for t in ALL_TICKETS]
    assert len(ids) == len(set(ids)), "duplicate ticket ids"


def test_classifier_system_prompt_names_all_three_categories():
    for cat in ("billing", "technical", "general"):
        assert cat in CLASSIFIER_SYSTEM


def test_classify_ticket_parses_a_clean_one_word_reply(monkeypatch):
    """classify_ticket must lowercase, strip whitespace and a trailing period, and
    flag whether the label is one of the three allowed categories — without a live call."""
    import providers_utils

    class FakeMessage:
        content = "Billing.\n"

    class FakeChoice:
        message = FakeMessage()

    class FakeUsage:
        prompt_tokens = 12
        completion_tokens = 2
        total_tokens = 14

    class FakeResponse:
        choices = [FakeChoice()]
        usage = FakeUsage()

    class FakeCompletions:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    result = classify_ticket(FakeClient(), "fake-model", "irrelevant text", temperature=0.0)
    assert result["label"] == "billing"
    assert result["valid"] is True
    assert result["total_tokens"] == 14


def test_gemini_client_raises_a_clear_error_without_a_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="GEMINI_API_KEY"):
        gemini_client()


@pytest.mark.skipif(not HAS_GROQ, reason="no Groq key in .env")
def test_live_groq_classifies_a_clear_ticket():
    client = groq_client()
    model = os.getenv("MODEL")
    tid, text = CLEAR_TICKETS[0]  # billing_clear
    result = classify_ticket(client, model, text, temperature=0.0)
    assert result["valid"], f"unexpected label: {result['label']!r}"
    assert result["label"] == "billing"


@pytest.mark.skipif(not HAS_GEMINI, reason="no Gemini key in .env")
def test_live_gemini_classifies_a_clear_ticket():
    client = gemini_client()
    model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
    tid, text = CLEAR_TICKETS[1]  # technical_clear
    result = classify_ticket(client, model, text, temperature=0.0)
    assert result["valid"], f"unexpected label: {result['label']!r}"
    assert result["label"] == "technical"


# ---------------------------------------------------------------- Gemini model picking (names rotate and retire)
STUDENT_LIST = ["models/gemini-2.5-flash", "models/gemini-2.5-flash-image", "models/gemini-2.5-flash-lite",
                "models/gemini-2.5-flash-native-audio-latest", "models/gemini-2.5-flash-preview-tts",
                "models/gemini-3-flash-preview", "models/gemini-3.1-flash-image", "models/gemini-3.5-flash",
                "models/gemini-3.8-flash", "models/gemini-3.8-flash-tts", "models/gemini-flash-latest",
                "models/gemini-flash-lite-latest", "models/gemini-omni-1.1-flash"]


def _fake_gemini(monkeypatch, ids):
    import providers_utils
    fake = type("C", (), {"models": type("M", (), {"list": lambda self: [type("X", (), {"id": i})() for i in ids]})()})()
    monkeypatch.setattr(providers_utils, "gemini_client", lambda: fake)


def test_list_gemini_models_drops_non_chat_models_and_the_models_prefix(monkeypatch):
    from providers_utils import list_gemini_models
    _fake_gemini(monkeypatch, STUDENT_LIST)
    names = list_gemini_models()
    assert "gemini-3.8-flash" in names and "gemini-flash-latest" in names
    assert not any(bad in n for n in names for bad in ("image", "tts", "audio", "omni")) and not any(n.startswith("models/") for n in names)


def test_pick_gemini_model_prefers_the_latest_alias_then_the_highest_plain_version():
    from providers_utils import pick_gemini_model
    assert pick_gemini_model(["gemini-2.5-flash", "gemini-flash-latest"]) == "gemini-flash-latest"
    assert pick_gemini_model(["gemini-2.5-flash", "gemini-3.8-flash", "gemini-3.5-flash", "gemini-3.8-flash-lite"]) == "gemini-3.8-flash"
    assert pick_gemini_model(["gemini-3-flash-preview"]) is None
    assert pick_gemini_model([]) is None
