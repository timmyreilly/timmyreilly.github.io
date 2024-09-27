---
title: "GitHub's Gitignore and Keeping DB Keys Safe"
date: "2015-05-11"
tags: 
  - "azure"
  - "code"
  - "github"
  - "gitignore"
  - "gitshell"
  - "powershell"
  - "python"
  - "studio"
  - "sublime"
  - "table"
  - "touch"
  - "visual"
---

I'm working with a raspberry pi and I'm learning how to collect and manage sensor data.

There is a lot of data and that's awesome, but dealing with remote persistent storage has helped me understand some good ways of keeping stuff organized and safe.

For example: 'Keys' or 'Tokens' (Not to be confused with the Late English writer Tolkien)

These are the keys to the door of your data. To access the contents behind these doors, you must establish that you are the key-holder. One of the ways to do this in software is to create a long complicated string that can passed to the database so you can input or output data.

As long as you keep this token secret nobody will be able to mess with your data, or use it without having to pay for it.

Now this sounds pretty simple, but what if you use that token in code that is stored in a public repository on GitHub? This is essentially like printing a bunch of keys to your house and leaving them all over town. Not safe or smart.

So...

**1.** We need to keep these keys separate from the rest of your code. **2.** We need to keep the file that contains those keys away from your public repository.

To do this I created a separate file called tokens.py that contains the strings of my tokens and a function called getStorageKey() that returns those strings. Cool, we've satisfied our first goal.

Now we need to keep this file away from our repository. To do this we create a .gitignore file. This is a special 'git' file that allows us to specify which files will not be added to the remote repository. To create a .gitignore file simply enter:

`touch .gitignore`

touch is a Unix command to create a file and update the access data, but not make any edits. Its the same as opening and closing without saving any changes.

After you've created this file you can edit it with any editor you like. I do it with [sublime](http://timmyreilly.azurewebsites.net/running-multiple-python-versions-on-windows/) or [VS Code](http://timmyreilly.azurewebsites.net/quick-edits-using-vs-code/) because it helps me keep track of the separation occurring between visual studio and GitHub.

All you need to do is add on a separate lines the files you don't want GitHub or just git to include.

When I first started all my .gitignore file had was:

`tokens.py`

Its expanded to include... `tokens.py *.pyc  # the asterisk* acts as a wild card and will match any files with .pyc at the end # anything that starts with a # is a comment and will be ignored from .gitignore`

I saved this file (.gitignore) then added and committed it to the repository.

Now any files I **add** that end in .pyc or match tokens.py will not be added to my repository. And you will not be prompted to add them when you check git status.

What about files we've already have added???

If we add the rule after we added the file we want to ignore... We need to remove it from tracking on GitHub using the rm --cache command.

This will not remove it from your computer, but it will stop if from being tracked by GitHub, and will essentially be treated as if it was removed from your repository.

To pull this off simply type this command

`git rm --cached filename.py`

In this case I'm removing a file named 'filename.py'. After checking our git status we'll see that this file is going to be removed.

Commit the changes and push to your remote repo.

You'll see the files are still in your local directory, but are no longer in the remote or local repository. Hooray for keeping things safe!

Please let me know if you have any questions or comments. The documentation is excellent and I recommend you spend some time reading through the resources below to round out your learning: [touch (Unix)](http://en.wikipedia.org/wiki/Touch_(Unix)) [GitHub .gitignore](https://help.github.com/articles/ignoring-files/) If you enter: 'git ignore --help' in your gitshell you can find more helpful documentation about using .gitignore Setting up Code for [Powershell](http://timmyreilly.azurewebsites.net/quick-edits-using-vs-code/) Setting up sublime for [Powershell](http://timmyreilly.azurewebsites.net/running-multiple-python-versions-on-windows/)

\[caption id="attachment\_4451" align="aligncenter" width="660"\]![SomeOfTheNorCalTeam]({{ site.baseurl }}/assets/images/WP_20150429_16_32_07_Pro-1024x577.jpg) Evangelists in their natural habitat. Behind a booth and with a computer. \[/caption\]

