# Student Handout - Session 2

## Agenda
1. Review Session 1 - Three Objects, Three Trees
1. Set up for Session 2 - Fork and clone
1. Common Git Workflows

## Set up for Session 2

Setup is straightforward: Just fork https://github.com/walquis/learning-git, and clone to a workspace
```
# After forking https://github.com/walquist/learning-git to your Github account...
$ cd
$ git clone https://github.com/<your-github-login-here>/learning-git.git forked-learning-git
# ...or, if you have SSH keys set up (note the colon)...
$ git clone git@github.com:<your-github-login-here>/learning-git.git forked-learning-git
```

## Common Git Workflows

### Forgot to pull before committing

I'm starting with this workflow because it's very common for me!

It typically goes like this: 
1. I cd into a repo workspace that I already have cloned, but haven't touched in awhile.
1. I make some changes and commit.
1. I 'git push'
1. Git rejects my updates with something like:

<blockquote>
<span style="color:red">! [rejected]</span> &nbsp; &nbsp; &nbsp; <span style="color:green">master -> master (non-fast-forward)</span><br>
<span style="color:red">error: failed to push some refs to 'git@github.com:walquis/learning-git'</span><br>
<span style="color:gold">hint: Updates were rejected because the tip of your current branch is behind<br>
hint: its remote counterpart. Integrate the remote changes (e.g.<br>
hint: 'git pull ...') before pushing again.<br>
hint: See the 'Note about fast-forwards' in 'git push --help' for details.<br>
</span>
</blockquote>

We'll re-enact this scenario in our own forked repos.  Let's start by moving our local master branch to one commit behind origin/master.  How would we do that?

OK, now let's change a file (e.g., add a line to git-aliases.sh), and add/commit/push.

What happened? What now?

A couple of options:
1. Pull-and-merge - valid, but creates a messy graph for no good reason
1. Reset-and-cherry-pick - makes the graph like you want it

```
$ git reset --hard HEAD^
$ git pull
$ git cherry-pick <sha-of-your-original-commit>
```

### Resolve Merge Collision

Let's make a merge collision happen: Branch, change the same line of a file, commit and try to merge.

1. First, find a change we want to collide with.  How about master?
```
$ git show # How about the .gitignore change?
```
1. Checkout a new branch that will lead to a collision (which commit should we branch from?)
1. Make a change that will collide (i.e., to line 45 in .gitignore).
1. Attempt to merge from master.
```
$ git config --global core.editor "code --wait"  # Set your editor to vscode
$ git merge master
Auto-merging .gitignore
CONFLICT (content): Merge conflict in .gitignore
Automatic merge failed; fix conflicts and then commit the result.
$ git status
$ code .gitignore
```

Git has modified our source file!

Note that vscode has added some helpful "phantom text"\--'(Current Change)' and '(Incoming Change)'\--to help clarify what's what. Note also, **that text isn't part of the file**.

When you've decided what the file should look like, 'git add' to tell git it's OK now (as git itself tells you when you do 'git status').

Then finish the merge with a 'git commit' (again, as 'git status' instructs)..

### Save Current Work and Return to it Later
```
$ git stash
$ git checkout -b someNewBranch   # Or some existing branch
...
$ git checkout master
$ git stash pop
$ git stash list
```

### Clean Up Commit History Before Pushing - [git rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing){:target="_blank"} 

This is another instance of using git to practice good communication skills.  Nobody wants to see my stumbling around; they just want to see the final draft.

Let's make a series of commits we don't want people to see...suppose we tweak test.sh to look for 'twentieth' instead of 'Wallace', just one line, and print out to the screen.

```
$ git rebase -i some-commit-prior-to-commits-to-fix
```

### Find a Bad Commit - [git bisect](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git){:target="_blank"}

Sometimes a bug creeps in and it's hard to find where it happened.

```
$ git help bisect   # You can also 'git help' any other git command.
$ git bisect start HEAD 99154bcc
$ grep Wallace text.txt # Bad if found, good if not
$ git bisect good
...
$ git bisect reset  # Go back to the head of the branch
```

This is effective, but a little tedious.  What if we could automate it...?
```
$ cat test.sh
$ bash test.sh
$ echo $?
$ git bisect start HEAD 99154bcc
$ git bisect run bash test.sh
```

## Miscellaneous
- 'git show' - By default, HEAD's diffs vs previous commit.  Can 'git show' any SHA.
