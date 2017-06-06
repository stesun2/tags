# Instructor Notes

Keep the [Session 1 Syllabus](syllabus-session-1) in mind, to make sure you've covered the terms and concepts listed there.

Themes:
- Git has your back.  (We'll see that most git-repo mistakes are recoverable)
  - Helps you keep a known good point for reference.
  - Lets you boldly try new things.
- If you're gonna do software: Know the bash command line, know git, and know Vim.

### Clone the learning-git repo
- !$
- -p option to mkdir

### Unpack the git objects that Github.com has packed
- directories starting with '.'
- commands starting with '.'
- the executable bit on files

### Activate git aliases, append to profile
- Describe what's happening

## Exploring the git repo - SHAs and objects

### The git database
- 'hash-object' and 'cat-file' are "plumbing" commands, not explicitly used in the normal course of git.
- Do you get the same value as I do when hashing hi.txt?  Why?
- Discuss address uniqueness: implications for storage e.g. identical files from different commits, different dirs.

### Storing objects in the git database
- 'echo' and 'cat' - does everyone know what they do?
- '-w' option writes the file to the database (compressed)..
- 1st two chars are dirname, the rest is filename.
- Usually, don't need to say the whole SHA; 4 chars minimum.

Answer to "Test your understanding": A git object is stored as a file whose name corresponds to the SHA-1 checksum of its content.

## The Three Git Objects
- '-t' option - type
- Touch on why their HEAD's SHA is now different than mine, even when committing the same file.
- Go over the attributes of each object type.
- Walk through drawing a diagram like [this diagram](https://git-scm.com/book/en/v2/images/data-model-3.png){:target="_blank"} of the 2 latest commits.


