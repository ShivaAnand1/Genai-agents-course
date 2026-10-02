# Session 10 - selection matrix output

expected EMI 17594.09, ratio 42.7%


## faq: Public product FAQ chatbot
1. gpt-oss-20b on Groq - score 90.0 - Rs 8,460/month - 1.5 s - Q3
2. Llama 4 Scout 17B-16E on Groq - score 86.0 - Rs 11,280/month - 1.5 s - Q3
3. gpt-oss-120b on Groq - score 83.1 - Rs 16,920/month - 2.0 s - Q4
4. Qwen3 32B on Groq - score 72.0 - Rs 26,282/month - 2.0 s - Q3
5. Frontier economy tier (closed, vendor API) - score 62.2 - Rs 62,040/month - 1.5 s - Q3
6. gpt-oss-20b self-hosted on a smaller GPU server - score 57.0 - Rs 65,800/month - 2.5 s - Q3
7. gpt-oss-120b self-hosted on your own GPU server - score 45.0 - Rs 188,000/month - 3.0 s - Q4
8. Frontier mid-tier (closed, vendor API) - score 38.9 - Rs 248,160/month - 3.5 s - Q4
9. Frontier flagship (closed, vendor API) - score 20.0 - Rs 620,400/month - 6.0 s - Q5
- excluded: Llama 3.1 8B Instant on Groq (a price is unknown - fill it in)
- excluded: llama3.2:3b on your laptop (Ollama) (cannot serve 20,000 calls/day (this setup tops out near 5,000))

## documents: Loan-document analysis (customer PII)
1. gpt-oss-20b self-hosted on a smaller GPU server - score 70.0 - Rs 65,800/month - 2.5 s - Q3
2. gpt-oss-120b self-hosted on your own GPU server - score 45.0 - Rs 188,000/month - 3.0 s - Q4
- excluded: gpt-oss-20b on Groq (data must stay on-prem; this model's provider sees the prompt)
- excluded: gpt-oss-120b on Groq (data must stay on-prem; this model's provider sees the prompt)
- excluded: Qwen3 32B on Groq (data must stay on-prem; this model's provider sees the prompt)
- excluded: Llama 4 Scout 17B-16E on Groq (data must stay on-prem; this model's provider sees the prompt)
- excluded: Llama 3.1 8B Instant on Groq (data must stay on-prem; this model's provider sees the prompt; quality 2 below the minimum 3; a price is unknown - fill it in)
- excluded: llama3.2:3b on your laptop (Ollama) (quality 2 below the minimum 3)
- excluded: Frontier flagship (closed, vendor API) (data must stay on-prem; this model's provider sees the prompt)
- excluded: Frontier mid-tier (closed, vendor API) (data must stay on-prem; this model's provider sees the prompt)
- excluded: Frontier economy tier (closed, vendor API) (data must stay on-prem; this model's provider sees the prompt)

## agent_assist: Call-centre agent-assist (live suggestions)
1. gpt-oss-20b on Groq - score 85.0 - Rs 13,324/month - 1.5 s - Q3
2. Llama 4 Scout 17B-16E on Groq - score 82.6 - Rs 18,274/month - 1.5 s - Q3
3. gpt-oss-120b on Groq - score 70.6 - Rs 26,649/month - 2.0 s - Q4
4. Frontier economy tier (closed, vendor API) - score 70.2 - Rs 95,175/month - 1.5 s - Q3
5. Qwen3 32B on Groq - score 59.3 - Rs 44,288/month - 2.0 s - Q3
6. gpt-oss-20b self-hosted on a smaller GPU server - score 39.6 - Rs 65,800/month - 2.5 s - Q3
7. gpt-oss-120b self-hosted on your own GPU server - score 22.5 - Rs 188,000/month - 3.0 s - Q4
- excluded: Llama 3.1 8B Instant on Groq (quality 2 below the minimum 3; a price is unknown - fill it in)
- excluded: llama3.2:3b on your laptop (Ollama) (too slow (8.0 s > 3.0 s); cannot serve 30,000 calls/day (this setup tops out near 5,000); quality 2 below the minimum 3)
- excluded: Frontier flagship (closed, vendor API) (too slow (6.0 s > 3.0 s))
- excluded: Frontier mid-tier (closed, vendor API) (too slow (3.5 s > 3.0 s))

## Measured
{'groq': {'ttft_s': 2.0, 'total_s': 2.06, 'tokens_per_s': 638.8, 'check': {'emi_ok': True, 'ratio_ok': False, 'score_out_of_2': 1}}, 'ollama': {'ttft_s': 9.99, 'total_s': 13.51, 'tokens_per_s': 11.9, 'check': {'emi_ok': False, 'ratio_ok': False, 'score_out_of_2': 0}}}