# Your work repository — steps and fixes

Two folders, two jobs. Never put one inside the other.

```
Documents\
  genai-agents-course\   <- the COURSE repo. You only ever  git pull  into it.
  genai-course-work\     <- YOUR repo. You  git add / commit / push  from it.
```

You need: a free GitHub account (github.com), Git installed (Session 9a), and your GitHub username.

## Steps

**1. Tell Git who you are (once per laptop).** Use the email address on your GitHub account.
```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global --list
```
**2. Create the repository on GitHub.** github.com -> **New** -> name it `genai-course-work` -> **Public** -> tick **Add a README file** -> **Create repository**. (It must be Public so your instructor can read it.)

**3. Clone it into Documents, next to the course repo.**
```powershell
cd ~\Documents
git clone https://github.com/<your-username>/genai-course-work.git
```
**4. Do the work.** In the notebook, run section 6: it creates `prompts/library.md`, `.gitignore` and a README inside `genai-course-work`. Set `SAVE = True` when your three prompts pass.

**5. Commit and push** (in a terminal, inside the work repo).
```powershell
cd ~\Documents\genai-course-work
git status
git add .
git commit -m "Session 14: prompt library v1"
git push -u origin main
```
The first push opens a browser window: sign in to GitHub. After that, plain `git push` works.

**6. Check it.** Refresh your repository page on GitHub: you should see `prompts/library.md`. Then run the notebook's last cell (the self-check): every line should say `PASS`.

Every future session: `git pull` in the **course** repo to receive files; `git add / commit / push` in **your** repo to hand work in.

## When something goes wrong

| You see | It means | Fix |
|---|---|---|
| `fatal: not a git repository` | You are in the wrong folder | `cd ~\Documents\genai-course-work` |
| `Author identity unknown` / `Please tell me who you are` | Step 1 not done | Run the two `git config --global user...` lines |
| `fatal: The current branch main has no upstream branch` | First push | `git push -u origin main` |
| `There is no tracking information for the current branch` (on pull) | Branch not linked to GitHub | `git branch --set-upstream-to=origin/main main` |
| `Repository not found` on push | Wrong URL, or you are signed in as a different GitHub account | `git remote -v` to read the URL. Windows search -> **Credential Manager** -> **Windows Credentials** -> remove entries starting `git:https://github.com` -> push again and sign in with the right account |
| `Updates were rejected ... fetch first` | GitHub has a change you don't (for example you edited the README on the website) | `git pull`, then `git push`. If a text editor opens asking for a message: save and close it (in vim: press `Esc`, type `:wq`, press `Enter`) |
| `nothing to commit, working tree clean` | You already committed | `git push` |
| Push worked but `prompts/library.md` is not on GitHub | The notebook wrote to a different folder | Check `WORK_REPO` in section 6 points at your cloned `genai-course-work` |
| The self-check says `.env` is tracked | You committed your secrets file | Run the fix it prints, and **create a new API key** — the old one may now be public |

**Never** copy `.env` into your work repository. The generated `.gitignore` already blocks it.
