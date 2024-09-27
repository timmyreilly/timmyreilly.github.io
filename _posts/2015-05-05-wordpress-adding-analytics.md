---
title: "Wordpress - Adding Analytics"
date: "2015-05-05"
---

Site tracking is cool because information is cool! This tutorial will show you how to configure analytics for a Wordpress blog by editing the Header.php file using FTP.


```html

```


**Let's imagine your company gave you something like this to begin analytics:** `<meta name="t_omni_extblogid" content="contosotextblogs" /> <meta name="t_omni_blogname" content="alias" /> <meta name="t_omni_market" content="US" /> <meta name="t_omni_audience" content="DEVELOPER" /> <script type="text/javascript" src="http://www.contoso.com/feeds/omni_external_blogs.js"></script> <noscript><a href='http://www.omnicron.com' title='Web Analytics'><img src='http://something.fancy.com'  height='1' width='1' border='0' alt='' /></a></noscript>`

&amp;amp;lt;a href='http://www.omnicron.com' title='Web Analytics'&amp;amp;gt;&amp;amp;lt;img src='http://something.fancy.com'&amp;amp;nbsp; height='1' width='1' border='0' alt='' /&amp;amp;gt;&amp;amp;lt;/a&amp;amp;gt;

The only thing you should have to change is the "alias" to your personal alias.

Of course I've edited this snippet because we don't won't everybody to add analytics to their blog…

Okay, so you have your snippet. **Where do you put it?**

Let's say your hosting your Wordpress blog on Azure. You have a number of different ways to access these files.

The simplest is probably using an FTP client such as WinScp. An FTP client will allow you to change files on the remote directory.

[Here's the link to download WinSCP](http://winscp.net/download/winscp572setup.exe):

After you install WinSCP you should see a page like this: ![WinSCP]({{ site.baseurl }}/assets/images/WinSCP.png)

Make sure you set the File Protocol to FTP.

**Now go to Azure** Here's the link to Azure: [http://portal.azure.com/](http://portal.azure.com/)

Now go into azure to find the Host Name, User Name, and Password ![FTPDashboard]({{ site.baseurl }}/assets/images/FTPDashboard.png)

In the current portal you'll find all the information on the Dashboard. You can find the FTP hostname and the Username about halfway down the page on the right.

And if you don't know your password you can set deployment credentials from the same page. Simply click here:

![resetdeploymentcreds]({{ site.baseurl }}/assets/images/resetdeploymentcreds.png)

Set your credentials, and remember your password.

![setcredspage]({{ site.baseurl }}/assets/images/setcredspage.png)

Now open WinSCP and enter your credentials alongside the FTP Host Name

![winscplogin]({{ site.baseurl }}/assets/images/winscplogin.png)

Now that you're logged in your can explore the files just like your regular file explorer! We're going to find the header file of your current theme and add the code snippet!

**Check the path and the highlighted file!**

![winscppath]({{ site.baseurl }}/assets/images/winscppath.png)

Now double click on that file to open it in your favorite text editor.

![VSEditHeader]({{ site.baseurl }}/assets/images/VSEditHeader.png)

_Here you can see where I've pasted in my code._

**Save the file and it will be saved on your Azure directory and you're ready to go!**

You can double check to see the changes. Go back to your azure portal and actually click on the FTP host link. This will open a new tab and will ask for the same credentials.

![ftpbrowser]({{ site.baseurl }}/assets/images/ftpbrowser.png)

Once inside you'll be able to explore the Directory contents in your browser.

Check the path at the top to see my current location and notice that I can open the file right here to check the contents!

![browserftp]({{ site.baseurl }}/assets/images/browserftp.png)

Looks good from here too!

![headerphpbrowser]({{ site.baseurl }}/assets/images/headerphpbrowser-1024x542.png)

Now everytime anyone opens a page on your blog data traffic data will be sent to your analytics platform.

Let me know if you have any questions!

\[caption id="attachment\_4291" align="aligncenter" width="2000"\]![The Kannon at //Build. This could be a really great story.]({{ site.baseurl }}/assets/images/WP_20150501_12_57_10_Pro.jpg) The Kannon at //Build.\[/caption\]

