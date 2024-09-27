---
title: "MEAN Stack on Ubuntu Server Setup"
date: "2014-11-20"
tags: 
  - "angular"
  - "azure"
  - "express"
  - "install"
  - "mean"
  - "mongo"
  - "node"
  - "on"
  - "server"
  - "setup"
  - "stack"
  - "ubuntu"
---

Let's say you're at your first hackathon. You have an idea you want to develop quickly and manage and deploy remotely so you're ready to scale, or aggregate data cross platform. Buzzwords.

I've seen it many times in my last 3 months of attending hackathons.

Students want to get started quickly without wasting time worrying about deployment and compatibility across devices this setup will also prepare them to work in a team because it'll allow deployment from Git. And these principles carry down into innovation initiatives happening at companies around the world one solution is MEAN.

Let's say you're new to web development and you're learning node but don't want to gunk up you machine with installations and moving files around before you have a grasp of what really matters.

That's where MEAN in the Cloud comes in.

So what we're going to do is install the MEAN stack on a cloud server so we can mess with code, learn, restart, and more without worrying about ruining our machine.

**_This whole process will take place in eight steps:_** **First:** [Setup Ubuntu Server](#1) **Second:** [Get into server](#2) **Third:** [Install Mongo](#3) **Fourth:** [Install Node](#4) **Fifth:** [Create first Node app](#5) **Sixth:** [Install NPM](#6) **Seventh:** [Install Express and Angular using NPM](#7) **Eighth:** [Get a tiny server running](#8) **_First: Setup Ubuntu Server_**

1\. Login to Azure ([Create an account](http://msdn.microsoft.com/en-us/library/dn168987(v=nav.70).aspx) if you don't have one already) Using azure isn't required any cloud hosting that provides and Ubuntu distro should work.

2\. In the bottom left click "New"

3\. Next to Compute Virtual Machine

4\. Select Quick Create

5\. Give it a name (eg. meanincloud)

6\. In IMAGE dropdown select 'Ubuntu 14.04 LTS'

7\. Leave the size at the default - you can always scale later.

8\. Provide a password and confirm it

9\. Select the region nearest to you.

10\. Hold tight, the cloud is provisioning resources and configuring your machine.

11\. After status reads running double click on 'meanincloud'

12\. Then select 'DASHBOARD'

13\. Scroll down until you see SSH details on the left.

14\. take note of those values it should be something like: 'youservername.cloudapp.net: 22" This is your server host name and the SSH port we'll be using this in the next section to access your remote machine

We now have a Linux VM with the Ubuntu distribution. This is our base on which we'll build the MEAN stack. _**Second: Get into Server**_

For this part we'll need an SSH client. Putty is what I've always used and works well for this instance. [Download page](http://www.putty.org/ "Download PUTTY! ")

1\. in the box labeled Host Name (or IP address) paste 'yourservername.cloudapp.net' and leave the port at 22.

2\. You'll likely receive a PuTTY security alert. That's cool for now, select Yes.

3\. If you're using azure you're login will be 'azureuser'

4\. And you're password will be that same that you provided at '7.' in the previous section.

5\. You're now at the Ubuntu terminal (Like cmd). You'll start at home, but you can get to root by entering: 'cd /' and back to home with 'cd ~'

6\. Now we get [MEAN](http://tamas.io/what-is-the-mean-stack/ "Clear Explanation") _**Third: Install Mongo**_

The Mongo installation instructions can be found [here](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/ "Try running the server at the bottom if you want to play around with Mongo") if you're curious. But we'll run through that here.

Note: All lines in bold will be run in the terminal. Copy and right click to paste into your putty shell. Then press enter to run the command.

1\. Import the public key used by the package management system: `**~$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10**`

2\. Create a list file for MongoDB `**~$ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list**` No result will display.

3\. Reload local package database. `**~$ sudo apt-get update**` You'll get about 15 seconds of output.

4\. Install the MongoDB packages - This will download the latest stable version, but you can be specific if you liked an older version. Read more into it here. **`~$ sudo apt-get install -y mongodb-org`** You'll get about 30 seconds of output.

5\. Reload local package database **`~$ sudo apt-get update`**

Alright! Mongo is installed, here's a great tutorial if you want to get a better understanding of how Mongo works. _**Fourth: Install Node**_

Node is the web app framework that you'll be building you application with. Although its not spelled MNEA or NMEA, this more accurately represents the priority of these tools.

1\. Install Node: **`~$ sudo apt-get install nodejs`**

2\. Confirm install with 'Y' About 20 seconds of output.

3\. Node is now installed you run node by entering nodejs this will take you to the Node REPL.

4\. Try it out **`~$ nodejs`**

5\. In the REPL you can run javascript `> console.log('hello world');`

6\. ctrl+c twice will exit the repl. _**Fifth: Create your first Node app**_

We now have everything we technically need to start development with Node, the first thing we'll do is create a hello world app to begin putting the pieces together.

1\. First install emacs24 an inline text editor for linux that will allow us to make changes to code inside our terminal. **`sudo apt-get install emacs24`** a 'Y' will be required to finish And we'll get about a minute of output. Now we can edit code right here! No need to worry about messing up your own file system.

2\. Make sure we're updated. **`~$ sudo apt-get update`**

3\. make a directory to hold our demo **`~$ mkdir mean-practice`**

4\. 'ls' will show us our newly created directory

5\. Change into that directory **`~$ cd mean-practice`**

6\. now we'll create our first file inside of that directory. **`/mean-practice$ emacs package.json`** This will open a new emacs view that will allow us to make changes, save ctrl+x+s and close ctrl+x+c.

7\. This is our basic manifest file. type this into it. `{ "name" : "mean-practice", "version": "0.0.1" }` This is the minimum. As you learn more about node you'll see what else will go in there. ctrl+x+s to save and ctrl+x+c to exit.

8\. Let's create our main file, basically our entry point for the application, and where the server will begin operating. **`/mean-practice$ emacs server.js`**

9\. put this into that file: `console.log("Hello World with NODE!");` Though possibly over-zealous this is our first node app! ctrl+x+s to save and ctrl+x+c to close.

10\. Type 'ls' to see what's in our mean-practice directory. Not a ton, but everything we need to start our application.

11\. Let's run our application: **`/mean-practice$ nodejs server`** Sweet! All we'll get as output is "Hello World with NODE!" but that's better than a kick to the face.

12\. To stop the server press **ctrl+c** _**Sixth: Install secret N, NPM**_

Node strengths and rapid growth are due in large par to the awesome npm. A package manager which will allow you to import a whole host of clever tools, apps, widgets, and formatting helpers to make your node development as easy as possible. So let's install that now.

1\. First install NPM. `**/mean-practice$ sudo apt-get install npm**` You'll need another 'Y' and expect about 45 seconds of output.

2\. Update again `**/mean-practice$ sudo apt-get update**` another 20 seconds of output _**Seventh: Now we'll install Express and Angular using NPM.**_

Now that NPM is installed we can add our final packages!

1\. Install express `**/mean-practice$ sudo npm install express --save**` express is in the npm system and --save will edit our package.json file to include the express module. [Click this link to find out more about express.](https://www.npmjs.org/package/express "Must read. ") Expect about 15 seconds of output.

2\. Enter ls to see our new directory 'node\_modules' where our node modules are being stored.

3\. Open package.json to see the changes in our manifest. **`/mean-practice$ emacs package.json`** You'll now see under dependencies "express" Yay! Now express is installed. ctrl+x+s to save and ctrl+x+c to exit.

4\. Now lets install [angular](https://www.npmjs.org/package/angular "Go read what angular is about! "). **`/mean-practice$ sudo npm install angular`** Now the angular module is part of our application! Click on the link above to learn more about Angular.

That's it! Now you have a MEAN stack ready for development!

Let's quickly build a simple server, configure an endpoint in azure and become a client with our browser. **_Eigth: Get a tiny server running_**

1\. Open our server.js **`/mean-practice$ emacs server.js`**

2\. Replace our hello world statement with:

`var express = require('express'); var app = express();  var port = 3000;  app.get('/', function(req, res) { res.send('hello from afar'); });  app.listen(port, function(){ console.log("Listening at port: " + port); })`

4\. Now our server.js is actually a server but our virtual machine doesn't know that. Go back to your azure portal.

5\. Select Endpoints at the top between monitor and configure.

6\. At the bottom select 'ADD'

7\. Select 'ADD A STAND-ALONE ENDPOINT'

8\. Press the arrow

9\. Under the NAME dropdown select HTTP

10\. Leave protocol at TCP

11\. Leave public port at 80

12\. Change the private port to '3000' We're mapping our endpoints improperly for this demo to keep things simple. As you learn more about web development you'll want to change your endpoints to accurately reflect what's happening in your server.

13\. Hit the checkmark.

14\. Back in your putty shell run the server! **`/mean-practice$ nodejs server.js`**

15\. Open a new tab in your browser and navigate to: 'yourservername.cloudapp.net'

16\. CHECK IT OUT! You've got a website running node on a virtual machine! Throw your hands in the air! You're ready to hack and learn.

Here are some learning resources to get you started. [JavaScript](http://www.codecademy.com/en/tracks/javascript "Code Academy will teach you in the browser! ") [Node](http://www.nodebeginner.org/ "Node Beginner Book") [Git will help you with pushing code to your VM](http://gitimmersion.com/index.html "Immersion! ")

\[caption id="attachment\_2241" align="aligncenter" width="474"\]![Always shoot for the Moon! ]({{ site.baseurl }}/assets/images/IMG_20140807_224627-1024x768.jpg) Always shoot for the Moon! or an asteroid, go Rosetta! \[/caption\]

