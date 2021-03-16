# Collaborating with git

## Introduction

In this two-session hands-on course, you will experience the essence of git by working in teams to improve a simple Python webapp, laying a foundation for collaborating in a professional environment.

This material has been presented to every CodePlatoon cohort since Bravo. Several graduates report that, equipped with a firm grasp of these git basics, they have become go-to git resources in their software engineering teams.

## About the instructor
As a devops professional with three-ish decades of experience in version control, I first experienced git in 2009 when developers insisted on bringing it into my company.  I learned a few basic survival commands, but it wasn't really clicking for me. Depressingly often, especially for a version control "expert", I got out of my depth and had to be rescued.  Eventually I tired of memorizing magic spells and decided to learn the basics of git once-and-for-all.  Suddenly, git started making sense!  That feeling of enlightenment inspired this course.

## In a nutshell - Three objects, Three trees
You will get lots of practice expressing your changes in terms of git's data model - **three objects** - and moving them around in git's state model - **three trees**.

The **three objects** are blob, tree, and commit.  The **three trees** are HEAD, index, and workspace.

## Tips for Success
- **Do the Prework** - The class moves fast, especially if you haven't done much with git, Bash, Peewee and/or Flask.  Doing the Prework is essential to help you keep up and get the most out of the time.
- **Stop me during the class and ask questions** - Really.  It helps me know how things are going.  And asking questions in a classroom environment, although often challenging, ends up helping others in the class.

## Session One - Explore the Tags app, Linux/Bash, and Git; set up your team
1. [Prework for Session 1](session-1-prework)
- Fork/clone the repo and get the app running.
- Explore the code.
1. [Syllabus for Session 1](session-1-syllabus)
1. [Student Handout for Session 1](session-1-handout)

## Homework - Between Session One and Session Two
You've set up your development environment, gotten the webserver up and running, and gone over the code.  (You've also considered the many nuances, meanings and contexts of the word 'environment'!).  Finally, you got an oh-so-brief intro to The Three Objects, and to The Three Trees.

Now for a bit of homework to sink in the concepts we've covered.  This will help hit the ground running in Session Two!

The object of this homework is twofold:
1. Familiarize with the two major concepts we touched upon at the end of Session One:
    a. The Three Objects - the git data model
    b. The Three Trees - managing local changes
2. Familiarize with the changes your team will be collaborating on making in Session Two.

BUT FIRST: If you were not able to get your app up and running: *Re-do the prework from the beginning.*  This includes deleting your fork on github.com, and forking and cloning a fresh repo (if you want to keep your old fork around for some reason, just rename the "tags" directory on your local machine to something else).  Please, let me know via Slack if anything is not working for you.

### Familiarizing with the Three Objects and Three Trees
Work through the [Session 1 Handout](session-1-handout).

### Familiarizing with changes to make
In the [Prework for Session 1](session-1-prework), you looked through the code.  Now in this homework, you will look through changes that correspond to project tasks.

Visit the [tags repo on Github.com](https://github.com/walquis/tags){:target="_blank"} and skim through the README, which gives a rough idea of what we'll be doing in Session Two.

For now, let's just look at the first task in "Round One": "Move the HTML into a Jinja2 template". This task could be done as shown in the ```origin/view_template``` branch in your repo.  (Of course, you and your project team can implement the task however you choose; this is just an example of how it could be done.)

NOTE: Be extra-sure you've forked/cloned a fresh copy of tags, otherwise your experience will almost certainly NOT line up with this guide!

There are a number of different ways to view changes:

The easiest way to view diffs is to just look at them on github.com:  Navigate to https://github.com/walquis/tags/tree/view_template (or visit https://github.com/walquis/tags and choose "view_template" from the branch dropdown).  Then click "Compare", directly under the green "Code" button, and just right of the "Pull Request" link.

Another set of diff'ing techniques is outlined in the tags repo's README, which involves studying diffs via the terminal window.  It's doable, but not a great visual experience; this is one time when Terminal Is Not Better.

A third way is to download [SourceTree](https://www.sourcetreeapp.com){:target="_blank"} (or another git GUI, such as Github Desktop--but SourceTree is quite good), and point it to your local tags repo.

![Viewing the Tags Repo in SourceTree](/images/tags-repo-in-sourcetree.png){:class="img-responsive"}

SourceTree nicely represents the branches that correspond to sample implementations of the tasks in the [Tags README](https://github.com/walquis/tags/blob/master/README.md){:target="_blank"}.

In SourceTree, browse the branches that implement the [Round One Tasks](https://github.com/walquis/tags/blob/master/README.md#round-one-tasks){:target="_blank"}.  Note that each round-one branch comes from master--so the diffs are independent of each other.

(Remember, your project team will be implementing these tasks yourselves, so it's not necessary to use these branches "as-is" or even at all.  They are just there to give a sense of the nature of the task.  When your project team gets going, feel free to make use of them as little or as much as you please.)

Notice that the two "Round Two" task branches are *not* branched from master, but from a round-one task, in order to highlight the changes that characterize those particular tasks.

If you like, try implementing a round-one change on master, committing your change, and viewing it in SourceTree (or with another method if you choose).

