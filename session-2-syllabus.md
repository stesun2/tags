# Syllabus For Session 2 - Git Workflows

## Overview

Having learned how to package local changes into git's Three Objects and move them among the Three Trees, we now move up a level.  In Session Two, we will use git to smoothly swap changes with our team and our Future Selves.

## Prerequisites

Review [Prework and References](prework-and-references) for Session 2.

## Goals

1. Gain a deeper understanding of what familiar git commands (such as 'git merge') are accomplishing.
1. Know how your chosen workflow should change the commit graph, and use git commands to make it so.
1. Gain confidence to make changes knowing that git has your back.

## Objectives

By the end of session 2, students will be able to...

### Explain these terms and concepts:
* branch
* remote
* fetch vs. pull
* fast-forward merge
* 'detached HEAD' state

### Use these commands in appropriate context:
* git branch
* git merge
* git stash
* git cherry-pick
* git rebase -i
* git bisect

## Some (but not all) Common Workflows

### Forgot to 'git pull' Before Committing and Pushing"

How to fix it without a confusing, purposeless merge in your graph: Use [git cherry-pick](https://git-scm.com/book/en/v2/Appendix-C:-Git-Commands-Patching){:target="_blank"}.

### Resolve Merge Collision

A walk through a typical merge collision; understanding what git is saying, and how to resolve the collision correctly.

### Fix branch

"Whoops, I've committed my stuff on the wrong branch!"

This is a case of making the graph look like you want it.  Use 'git branch' and 'git reset' to put your changes where they should go, and restore the branch to what it should be.  For instance...

```
# Make some changes on master, add/commit.  Repeat.
$ git checkout -b myChanges
$ git reset --hard origin/master  # Assuming that's where you started.
```

### Save Current Work And Return to it Later 

"I need to save what I'm working on and come back to it later" - [git stash](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning){:target="_blank"}

### Clean Up Commit History Before Pushing - [git rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing){:target="_blank"}

### Find a Bad Commit - [git bisect](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git){:target="_blank"}

<hr>
You can follow along in the [Session 2 Student Handout](session-2-handout).
