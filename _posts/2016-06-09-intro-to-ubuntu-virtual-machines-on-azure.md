---
title: "Intro to Ubuntu Virtual Machines on Azure"
date: "2016-06-09"
tags: 
  - "azure"
  - "connection"
  - "iaas"
  - "intro"
  - "js"
  - "machines"
  - "microsoft"
  - "node"
  - "putty"
  - "python"
  - "ssh"
  - "ubuntu"
  - "virtual"
  - "vm"
---

When I search: Node JS Server Azure, Ubuntu, JavaScript, Mongo, Postgres, Flask, VM I turn up with all sorts of unhelpful results. So I dedicated a couple days to creating a couple guides for common Cloud Stacks on Azure VMs to make it as simple as possible to start deploying your code to the cloud.

This is the introduction and at the bottom of this blog post you'll see other workflows fill in.

So, Here's a guide to deploying an Ubuntu VM on Azure: 1. Gather Materials 2. Create VM 3. Check VM using SSH

**1\. Gather Materials** Here's what you'll need: [An Azure Account](https://azure.microsoft.com/en-us/free/?b=16.18) An SSH Client perhaps [putty](http://www.putty.org/)... or even [Bash On Windows](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)?

**2\. Create VM**

Head into the Azure Portal: [portal.azure.com](http://portal.azure.com/)

And Select Virtual Machines -> Then 'Add' ![selectVirtualmachines]({{ site.baseurl }}/assets/images/selectVirtualmachines.png)

You'll then see a page like this: ![selectubuntu]({{ site.baseurl }}/assets/images/selectubuntu.png)

Select Ubuntu Server 14.04.

There are lots of configurable deployments available if you feel like exploring.

Then select Create, but make sure the deployment model is Resource Manager as its more future ready then the classic model: ![createvm]({{ site.baseurl }}/assets/images/createvm.png)

We'll then get to the basic configuration tab, fill out the info and pick a User name and Password that you'll remember because you'll need it later!

![configurationbasics]({{ site.baseurl }}/assets/images/configurationbasics.png)

If you're not familiar with Resource Groups check out [THIS ARTICLE](https://azure.microsoft.com/en-us/documentation/articles/resource-group-portal/#manage-resource-group)

I've named my resource group: ResourceGroupOne

Hit Okay to go to the next configuration pane

Select the Size of your VM. To see all the options select 'View All' ![selectvmsize]({{ site.baseurl }}/assets/images/selectvmsize.png)

We're going to go with the cheapest option A1 Standard: ![SelectAOne]({{ site.baseurl }}/assets/images/SelectAOne.png)

Hit Okay to take us to our final configuration Pane, "Settings".

![settingstwo]({{ site.baseurl }}/assets/images/settingstwo.png)

There are a number of different settings presented here.

First up is Storage: This will configure what we want to name the storage account for our vm. I've changed mine to 'resourcegrouponestorage', but I could have selected any of my previous storage account in the same region, in this case westus.

Second is Network: We can configure a Virtual Network to allow our virtual machines to connect to other resource on our network by default. We can also change this later. So in this case I'm creating the default virtual network.

Again, I could have selected a previously created Virtual Network Called 'Databases' which is in the same region. ![virtualnetworkdefault]({{ site.baseurl }}/assets/images/virtualnetworkdefault.png)

Third is Extensions: We won't add any extensions

Fourth is Monitoring: Which we'll disable for simplicity sake, but is a very powerful tool one you start needing to make scaling decisions.

Fifth and finally is Availability: We won't use an availability set, until we need to scale out our app.

Here's what the lower portion of our settings pane looks like: ![settingstwoend]({{ site.baseurl }}/assets/images/settingstwoend.png)

And we'll select OK to finish with our settings. This will take us to the summary page so we can do a one more check on our machine, don't get to anxious about making mistakes because we can always tear this one down and spin up another if we messed something up! ![vmsummary]({{ site.baseurl }}/assets/images/vmsummary.png)

Hit Okay one last time!

You'll then be taken to your dashboard where you'll see a nice loading tile: ![loadingdashboard]({{ site.baseurl }}/assets/images/loadingdashboard.png)

It'll take ~5 minutes to spin up and then we'll be ready to take on the world!

Once ready it'll look like this: ![clickthetile]({{ site.baseurl }}/assets/images/clickthetile.png)

Click the tile to hit the landing page for our VM: ![vmnumberonelandingpage]({{ site.baseurl }}/assets/images/vmnumberonelandingpage.png)

See that public IP address? We'll use that to SSH into our machine.

In my case: 13.88.180.170 !

**3\. Check VM using SSH**

Let's SSH into our box.

Pull out your preferred SSH client. Here's bash on Windows and Putty Side by Side: ![sshintomachine]({{ site.baseurl }}/assets/images/sshintomachine.png)

Notice 'Timothy' Triple underlined? That's the User Name we set during basic configuration and is paired with the password that we also set in Azure.

When you connect you might have to accept the ras2key fingerprint. It'll look like this when using putty. Or it'll be in the terminal using bash. Type 'yes' or Select Yes to continue. ![sayyestowarning]({{ site.baseurl }}/assets/images/sayyestowarning.png)

Then type in your password and marvel and your creation: ![typeinyourpassword]({{ site.baseurl }}/assets/images/typeinyourpassword.png)

Let's test our vm by installing updates! Yay Updates!

`$ sudo apt-get update` ![sudoaptgetupdate]({{ site.baseurl }}/assets/images/sudoaptgetupdate.png)

Now that you have a VM ready let's put it to work! **[Host a Node Server](http://timmyreilly.azurewebsites.net/running-node-and-express-on-ubuntu-vm/) [Host a Python Flask Server](http://timmyreilly.azurewebsites.net/running-flask-on-ubuntu-vm/)**

\[caption id="attachment\_7941" align="aligncenter" width="4032"\]![Pradeep Cruising on National Donut Day ]({{ site.baseurl }}/assets/images/IMG_20160603_223007.jpg) Pradeep Cruising on National Donut Day \[/caption\]

