---
title: "First Login with Raspberry Pi using Windows 10"
date: "2015-01-02"
tags: 
  - "10"
  - "adafruit"
  - "b"
  - "console"
  - "pi"
  - "plus"
  - "raspberry"
  - "serial"
  - "usb"
  - "windows"
---

Since I'm now running full steam with [Windows 10](http://windows.microsoft.com/en-us/windows/preview "Free! ") I have run into a couple understandable documentation issues for the raspberry pi B+.

I'll be doing my best to fill them out as I learn about this device. So far no major issues, but one thing to clear up.

Consider this a Windows 10 companion article to [Adafruit's Console Cable guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview "Adafruit!").

The raspberry pi made it to me faster than the HDMI cord did, so I had no way to see what was happening on the device.

Luckily I purchased the Pi as part of a [kit from Adafruit](http://www.adafruit.com/products/2125 "100 Bucks! ") and it contains a console cable. A cool way to get to your Raspberry Pi's console and start learning about the device.

So I was following along with this tutorial from Adafruit. And found this warning. ![Capture]({{ site.baseurl }}/assets/images/Capture.png)

But I went ahead and gave it a shot.

- [Going to this site](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225&pcid=41 "Prolific Drivers")
- Clicking on the PL2303\_Prolific\_DriverInstaller\_v1.10.0.zip
- Saving it and extracting it to a folder on my desktop
- Running the PL2303\_Prolific\_DriverINstaller\_v1.10.0.exe
- Plugging in the GPIO leads**\***
- Plugging the USB end into my computer
- Finally Viewing the device in my device manager**\*\***.

![CaptureDevice]({{ site.baseurl }}/assets/images/CaptureDevice.png)

There it is under COM3!

I continued with the instructions given by Adafruit for [PuTTY](http://www.putty.org/ "Putty Download Page") configuration**\*\*\***.

Remember the default username is 'pi' and the password is 'raspberry' **\*** I found this diagram and site helpful for understanding what the differences were between the B and B+ GPIO ports. [Its from Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/ "Diagrams are Good"). ![Raspberry-Pi-GPIO-Layout-Model-B-Plus]({{ site.baseurl }}/assets/images/Raspberry-Pi-GPIO-Layout-Model-B-Plus-313x1024.png)

**\*\*** You can view exactly which port to use in the device manager which can be found by right clicking on the start menu.

**\*\*\***[I would suggest pinning PuTTY to your start menu](http://timmyreilly.azurewebsites.net/pin-putty-exe-to-start-menu/ "Pin Putty.exe to Start Menu In Windows 10") because I tend to lose it and it is great to have on hand when needing to SSH in [Azure](http://azure.microsoft.com/en-us/ "Azure Home Page"), Linux Server, or any other place you need to get Console/Terminal access.

\[caption id="attachment\_2781" align="aligncenter" width="1728"\]![Merry Retro Christmas from my Mom and her Brothers and Sisters from long ago!]({{ site.baseurl }}/assets/images/SCAN0322.jpg) Merry Retro Christmas from my Mom and her Brothers and Sisters from long ago!\[/caption\]

