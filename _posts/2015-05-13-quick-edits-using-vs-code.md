---
title: "Quick Edits Using VS Code"
date: "2015-05-13"
tags: 
  - "10"
  - "chang"
  - "code"
  - "edit"
  - "files"
  - "gitignore"
  - "power"
  - "powershell"
  - "profile"
  - "proj"
  - "shell"
  - "studio"
  - "visual"
  - "vs"
  - "windows"
  - "windows-10"
  - "yun"
---

I've been working in Visual Studio pretty heavily in the last two weeks, but every once in a while I need to make quick edits to my .gitignore file, which isn't in my project directory.

I usually open up a small text editor right from PowerShell and now that VS Code is out I thought 'why not use that?'

Here's how you can easily open files using code from PowerShell in three steps: **1.Find the path to VS Code 2. Edit your PowerShell profile 3. Open Files!** **1\. Find the VS Code Path**

First thing we need to do is find where VS Code is in our directory.

If you have Code pinned to your start menu or on your desktop simply right click the icon and 'select open file location'.

File explorer should now open to the location of the .exe. Right click the Code.exe file and select 'properties'.

If you selected a Shortcut Icon you should see a screen like this:

![vscodeshortcutpath]({{ site.baseurl }}/assets/images/vscodeshortcutpath.png)

If you navigated to the actual location in directory of VS Code it should look like this:

![vscodelocationpath]({{ site.baseurl }}/assets/images/vscodelocationpath.png)

Now right click and copy the path.

In my case: C:\\Users\\tireilly\\AppData\\Local\\Code\\app-0.1.0

**2\. Edit our PowerShell profile**

To edit our profile we need to find the Microsoft.PowerShell\_profile.ps1 file.

My file is located here:

![profilelocationpowershell]({{ site.baseurl }}/assets/images/profilelocationpowershell.png)

I open the file in notepad to make my edits:

![notepadpowershellprofile]({{ site.baseurl }}/assets/images/notepadpowershellprofile.png)

Now that we have our profile open we'll create an alias for labeled code followed by the path to our .exe eg: Set-Alias code 'C:\\Users\\user\\AppData\\Local\\Code\\app-0.1.0\\Code.exe

noticed how I added the Code.exe to the path so the program will launch!

Here's a photo of my current PowerShell profile for reference:

![powershellprofile]({{ site.baseurl }}/assets/images/powershellprofile.png)

Now we can save and close this file and open a new PowerShell window!

**3\. Edit some files!**

Let's edit our PowerShell profile with Code this time!

![symmetryisgood]({{ site.baseurl }}/assets/images/symmetryisgood.png)

Something oddly satisfying about getting exactly what you want with words.

![codeeditorpowershellprofile]({{ site.baseurl }}/assets/images/codeeditorpowershellprofile.png)

And there we go. The brand new Code editor at your fingertips whenever you need it!

Let me know if you have any comment or questions!

\[caption id="attachment\_4601" align="aligncenter" width="660"\]![Amazing Dude]({{ site.baseurl }}/assets/images/WP_20150423_21_13_35_Pro-1024x577.jpg) Professor Chang Yun is an excellent man with an amazing imagine cup record. His mentorship has led teams to US finals for 8 years straight. With 6 teams making it into the World Finals.\[/caption\]

