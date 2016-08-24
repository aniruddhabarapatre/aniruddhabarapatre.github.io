---
title: How to resolve fatal&#58; remote origin already exists
date: 2015-06-17 20:24 EDT
tags: Git, Github
Category: Blog
---

The error message indicates, there is already a remote configured with the same name. So you can either add the new remote with a different name or
update the existing one if you don't need it.

First of all Github has a good documentation on [renaming a remote](https://help.github.com/articles/renaming-a-remote/) to help
with this issue.

Check your remote repositories that you're connected to

    git remote -v

This should return a list in following format

    origin  git@github.com:github/git-reference.git (fetch)
    origin  git@github.com:github/git-reference.git (push)

That might help you figure out what the original 'origin' pointed to.

At this moment you could follow either of the below methods to resolve this error based on your requirements.

+ Remove the origin and your new repository as in

    git remote rm origin
    git remote add origin newrepo-url

+ If you want to keep the remote connection that you see with the -v, but still want to follow the workflow without having to remember 'github' (or some other name) for your repo, you can rename your other repository with the command:

    git remote rename [current name] [new name]

as in:

    git remote rename origin oldreponame

Once done, you should be able to change origin to new repository with

    git remote add origin newrepo-url

+ You could also use a new name for remote url as

    git remote add github newrepo-url

Remember though, everywhere now onwards you'd be using `github` as your remote name.
For example `git push origin master` should now be `git push github master`.
