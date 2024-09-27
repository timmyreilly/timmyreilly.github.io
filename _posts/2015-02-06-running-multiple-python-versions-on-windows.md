---
title: "Running Multiple Python Versions on Windows"
date: "2015-02-06"
tags: 
  - "alias"
  - "awesomeness"
  - "powershell"
  - "profile"
  - "python"
  - "shortcut"
---

So, you are learning to develop with Python and you keep hopping back and forth from Python 2.x and Python 3.x and possibly versions in between.

Beside running everything in a virtual environment, its sometimes nice to just get to the different REPLs to test tiny pieces of code.

This can be managed easily in powershell using powershell profile. [This link](http://www.howtogeek.com/126469/how-to-create-a-powershell-profile/ "Thanks Think Geek!") helped me learn about what it is and how to set it up.

But basically, you establish shortcuts by customizing a profile page with the things you need to access quickly.

Currently in my Profile I have a shortcut for starting Python27, Python34, and Sublime.

I'll show you how I set it up. First we'll edit our Profile, then we'll change the execution policy to allow this file to edit PowerShell.

Open powershell!

\[sourcecode language="•powershell"\]\[/sourcecode\]

1\. Type the following command and press ENTER:

`Test-Path $profile`

2\. If False you need to create a profile, if true go to step 3:

`New-item -type file -force $profile`

3\. Go to you PowerShell Directory. Step 2 will show the path to the location. For me its Users\\tireilly\\Documents\\WindowsPowerShell.

4\. Open your profile:

`Notepad .\Microsoft.PowerShell_profile.ps1`

5\. Now in Notepad you can add your aliases.

This is what I have: `Set-Alias subl 'C:\Program Files (x86)\Sublime Text 2\sublime_text.exe' Set-Alias python34 'C:\Python34\python.exe' Set-Alias python27 'C:\Python27\python.exe'`

Make sure you have the proper path to your existence of python. I have mine in my Root directory.

Now to activate this you need to set the execution policy to allow this to be activate each time you open powershell.

To do this follow these steps:

1\. Determine your current execution policy.

`Get-ExecutionPolicy`

This is just to double check you are restricted either way set it again to be sure.

2\. Set Execution policy for yourself.

`Set-ExecutionPolicy -Scope CurrentUser`

3\. You'll be prompted with "ExecutionPolicy: " Set it as unrestricted It should look like this: `ExecutionPolicy: Unrestricted"` Press enter.

4\. Comfirm by entering 'Y' and pressing enter again.

Now Restart Power shell and try typing in your alias! Does Python Start?

If not, I'm happy to help if you have any questions.

\[caption id="attachment\_3341" align="aligncenter" width="660"\]![This Photo is from 2010... Just saying]({{ site.baseurl }}/assets/images/IMAG0179-1024x683.jpg) This Photo is from 2010...\[/caption\]

