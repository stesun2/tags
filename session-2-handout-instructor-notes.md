# Instructor Notes, Session 2

Keep the [Session 2 Syllabus](syllabus-session-2) in mind, to make sure terms and concepts listed there are covered.

Themes for Session 2:
- Make your repo graph look like you want it to look.

### Forking the learning-git repo
- Explain why forking is necessary (because you don't have permission to commit into my repo!)
- Discuss https vs SSH protocol

### Forgot to pull...
- "How would we \[move local master back\]".  git reset --hard HEAD^
- Options
  - Pull-and-merge - It would work, but make your graph messy for no good reason.  (Discuss communication aspect)
  - Reset-and-cherry-pick - Better, because it's how you wanted it to look originally.
- How to remember the sha of the original commit?  (Scroll back, git reflog, make a branch before resetting).


