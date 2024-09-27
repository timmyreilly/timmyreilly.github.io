---
title: "Running Node and Express on Ubuntu VM"
date: "2016-06-09"
tags: 
  - "azure"
  - "express"
  - "iaas"
  - "ip"
  - "machine"
  - "microsoft"
  - "node"
  - "npm"
  - "nvm"
  - "virtual"
  - "vm"
  - "website"
---

So you just spun up your first Ubuntu Virtual Machine? No... Let's fix that: ["Intro to Ubuntu on Azure"](http://timmyreilly.azurewebsites.net/intro-to-ubuntu-virtual-machines-on-azure/)

YEAH! Let's put it to work!

The Basic Steps to using node on an Azure VM: 1. Open the Port 2. Install Git and Install Updates 3. Install Node and NVM 4. Code and Install Express 5. Run it and check it out! 6. Use forever to keep it alive

1\. Open the Port We're not talking battleships or submarines we're talking Infrastructure as a Service. Visit the landing page for your Ubuntu Virtual Machine: ![vmnumberonelandingpage]({{ site.baseurl }}/assets/images/vmnumberonelandingpage.png)

And select the resource group in the top left corner: ![resourcegroup]({{ site.baseurl }}/assets/images/resourcegroup.png)

Resource groups are the way we break down how our VM interacts with the internet, other vms, storage, and public/private networks.

To open the port we need to change our network security group which is represented by the shield. (Underlined in the above screenshot) Then we'll select settings -> Inbound security rules ![networksecuritygroupsettings]({{ site.baseurl }}/assets/images/networksecuritygroupsettings.png)

This will allow us to open up our VM to the Public Internet so we can visit it like any other website.

Under 'Inbound security rules' SSH is already included: ![defaultssh]({{ site.baseurl }}/assets/images/defaultssh.png)

We're going to add a new Inbound security rule named ExpressServerPort where we'll set the Destination port range to 3000 which we'll see later when starting our server. Here's the configuration pane for our ExpressServerPort: ![destinationport]({{ site.baseurl }}/assets/images/destinationport.png)

**2\. Install Git and Check Updates** Git is fun!

SSH into our Virtual Machine like we did in the VM intro then enter: `$ sudo apt-get install git` ![sudoaptgetinstallgit]({{ site.baseurl }}/assets/images/sudoaptgetinstallgit.png)

Yay! We have Git

Let's run our update command just to double check we're up to date:

`$ sudo apt-get update` ![sudoaptgetupdate]({{ site.baseurl }}/assets/images/sudoaptgetupdate.png)

Great let's move on with Node!

**3\. Install NVM and Node**

First NVM: [https://github.com/creationix/nvm](https://github.com/creationix/nvm)

NVM is a version manager for Node you can install using curl: Enter this command to install it: `$curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.1/install.sh | bash`

Then source your profile to add it to your commands: `$ source ~/.profile`

Then check out the version to make sure it installed: `$ nvm --version`

It should look like this: ![nvmisntallversion]({{ site.baseurl }}/assets/images/nvmisntallversion.png)

NVM is installed! Let's install a version of Node! `$ nvm install 5.0`

Then check our version of Node: `$ node -v` ![nvminstallfive]({{ site.baseurl }}/assets/images/nvminstallfive.png)

Sweeeeeeet

Check out NVMs readme on the github for more commands: [https://github.com/creationix/nvm](https://github.com/creationix/nvm)

With node comes 'npm' which allows us to install a whole bunch of node awesomeness. One of the more popular packages is express a minimalist web framework, we'll install this to start coding away.

**4\. Code and Install Express**

We'll be following along "Express's" introduction if you get lost/have more questions about express. [http://expressjs.com/en/starter/installing.html](http://expressjs.com/en/starter/installing.html)

First let's create our a directory, cd into it and initialize our app using nom. `$ mkdir myapp $ cd myapp $ npm init`

After entering `npm init` we'll be walked through a configuration step for our app. The only one that matters for now is (index.js) which will be the entry point for our app everything else can be the default for now.

If you were actually going to submit/share this code you'd want to accurately fill out this info.

After the initialization step we'll add express and list it as a dependency: `$ npm install express --save`

Here's what those steps look like: ![mkdirmyapp]({{ site.baseurl }}/assets/images/mkdirmyapp.png)

Weeee now have express and an app ready for your code!

Lets open `nano` and put the helloworld sample into index.js

`$ sudo nano index.js`

![sudonanohelloworld]({{ site.baseurl }}/assets/images/sudonanohelloworld.png)

Now lets run our app! `$ node index.js` ![nodeindexjs]({{ site.baseurl }}/assets/images/nodeindexjs.png)

Now that its running lets visit it by entering the IP address and port number into our browser. In my case the URL is: http://13.88.180.170:3000/ ![ipaddressandport]({{ site.baseurl }}/assets/images/ipaddressandport.png)

Neat!

**6\. Use forever to keep it alive** Unfortunately, if we close our Terminal/SSH Connection our project will stop running. To solve this, we use another NPM package called forever. [Here's the link to the repository with clear instructions.](https://github.com/foreverjs/forever)

In short we install it globally: `$ sudo npm install forever -g`

Then start it: `$ forever start app.js`

And stop it: `$ forever stop app.js`

That's it for now!

Now clone one of your node projects and run them in the cloud! Happy Hacking!

\[caption id="attachment\_8041" align="aligncenter" width="4032"\]![When the Male Roommates are home alone...]({{ site.baseurl }}/assets/images/IMG_20160513_215918.jpg) When the Male Roommates are home alone...\[/caption\]

