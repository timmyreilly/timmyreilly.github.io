---
title: "Pythons and Visual Studio Development"
date: "2014-10-23"
tags: 
  - "exe"
  - "27"
  - "34"
  - "gem"
  - "multiple"
  - "python"
  - "pythons"
  - "runserver"
  - "tidbit"
  - "versions"
---

Two little gems for today.

To run several versions of Python on a windows machine, install whatever versions of python you want, but don't add them to your path variable. (This will be an option on the second page of the python installer.)

Instead when you want to run a version of Python, call directly to the exe. **ie:** C:/Python27/python.exe or C:/Python34/python.exe

This way you can play with all the Pythons you want! Next is creating a shortcut for this because writing this every time is a bit tedious. Any tips?

**Next Tidbit** If you're using visual studio to develop a python project. You don't have to run it with python. Simply open command prompt or powershell to the visual studio directory and it acts like any other file system.

**eg:** I'm learning Django web framework, but I'm learning from tutorials that are agnostic, so I wasn't sure if I was going to learn how to run the server or complete unit tests.

But no problems so far. Just treat visual studio like Sublime, and use a command prompt to test your code.

This is how I'm running my server from the command prompt! C:/Python27/python.exe manage.py runserver

I'm run this below the .sln level Djangoapp.sln Djangoapp <---- CD into this file and run.

Hooray!

\[caption id="attachment\_1581" align="aligncenter" width="474"\][![THINK]({{ site.baseurl }}/assets/images/WP_20141016_005-1024x576.jpg)](http://www.computerhistory.org/) IBM has fight songs. Early adopter of "Company Culture"  
Lots of awesome stuff at the Computer History Museum: Click on the photo to find out more. \[/caption\]

