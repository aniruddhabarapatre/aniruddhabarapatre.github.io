---
title: How to kill process and free port
date: 2015-05-31 10:59 EDT
tags: Terminal, Middleman
Category: Blog
---

While setting up this blog for once I got into error where it was
erroring when I tried to start the server using `middleman server`
command.

The error was -

    Port 4567 is unavailable. Either close the instance of Middleman already running on 4567 or start this Middleman on a new port with: --port=4568

This error meant I messed up in one of my earlier session and may have
closed my terminal while server was running.

This is easy to resolve, by first finding the PID of the process.

    $ lsof -wni tcp:4567

Then use the number in the PID column to kill the process (in my case it
was 44995)

    $ kill -9 44995

Hope this helps anyone having issues freeing port.
