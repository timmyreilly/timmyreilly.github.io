---
title: "Generating an SSH Key and Using it on Azure"
date: "2016-11-03"
tags: 
  - "addresses"
  - "azure"
  - "bash"
  - "cloud"
  - "codes"
  - "generate"
  - "help"
  - "ip"
  - "key"
  - "keygen"
  - "keys"
  - "machines"
  - "private"
  - "public"
  - "server"
  - "solution"
  - "ssh"
  - "ssh-keygen"
  - "tutorial"
  - "ubuntu"
  - "vm"
  - "windows"
---

SSH KEYS allow us to connect to VMs without using passwords but by passing a private key that can be managed by you or your organization.

[For more about SSH](https://en.wikipedia.org/wiki/Secure_Shell)

There are three parts to this tutorial: A. Generate an SSH Key B. Create a VM in Azure that uses the public key C. Connect to VM using SSH keys

Prerequisites: Bash ssh-keygen (`$ info ssh-keygen` to learn more) An Azure Subscription

**A. Generate an SSH Key**

Open bash and enter: `$ ssh-keygen -t rsa -b 2048 -C "Ubuntu@azure-server"` Keyname: server-key Passphrase: somethingMemorable

Copy the contents of server-key.pub `$ cat server-key.pub`

Should look like this: `ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMlUr7PCEdBmCVZHG5RqI8i7GgYAzd2G/FZ987XXa63vnqxZmZogVmmXrTnBHeM6oDv7v7g495CiiiINhJbGR4o7t4agiHOM43egDv7BbiViTlfVr3y5AxLUvRwHnC3egl8ABVX1anfXXR73x7IS3YRNWkh6gXtlhImw8UKG04UoZEmWB9BLt53lk/9c3Hxz22YZarzImrpQYy1XEUZ096B9mK/Fe+/McH78ZHUpXEgOZBIDP5KdqPk5XKznpwUDJ4/SPXPEWWCCjQ8gOoTFcFMaiMnXp5o5Udsi/DFO1TS/t8BeCRymkr5tdPvzexjkjkjkjkjkjkjkjkjkjkjkjt Ubuntu@azure-server`

Here's what it looks like for me: ![keygenandcat]({{ site.baseurl }}/assets/images/keygenandcat-1024x581.png)

Cool and you'll also notice that there's another file in that same directory - server-key `$ ls | grep server` Here's what that looks like for me: ![lskeys]({{ site.baseurl }}/assets/images/lsKeys.png)

Now that we have our public and private keys let's get our VM setup.

**B. Create a VM in Azure that uses the public key**

1\. Go to the Azure Portal

2\. Select New -> Search: Ubuntu Server (I'm using 14.04 this time) ![selectubuntu1404]({{ site.baseurl }}/assets/images/SelectUbuntu1404.png)

3\. Make sure you've selected Resource Manger and click Create: ![resourcemanagecreate]({{ site.baseurl }}/assets/images/resourcemanagecreate-1024x446.png)

4\. Now configure the basics per our ssh-keygen parameters Name: azure-server VM Disk Type: Up To You User name: Ubuntu Authentication type: SSH public key SSH public key: Paste the results of `$ cat server-key.pub` Subscription: Depends how you want to pay for the server Resource Group: Up to you - I'm going to create a new one so I can quickly delete it. Location: Up to you

Should look like this: ![basicsconfigurationforssh]({{ site.baseurl }}/assets/images/basicsConfigurationforSSH.png)

Then select OK to go to the next section.

5\. Choose Virtual Machine Size I'm going with the smallest VM for testing. You can also view all different VM sizes to find the right one for your use case. ![pickvmsize]({{ site.baseurl }}/assets/images/PickVMSize.png)

6\. Configure optional Features Setting the Storage account name to something you'll remember easily is good. And if you want to configure ports now you can select Network Security group to allow ports specific traffic. Here's what that looks like: ![optional-azure-settings]({{ site.baseurl }}/assets/images/optional-azure-settings-1017x1024.png) Click okay to continue to the Summary of your VM.

Here's our summary: ![summary-click-okay-to-create-vm]({{ site.baseurl }}/assets/images/summary-click-okay-to-create-vm-929x1024.png)

Select okay to start your VM.

7\. Wait for it to be ready. Dashboard will have an icon and you'll get a notification when its ready: ![waiting-for-vm-to-spin-up-from-dashboard]({{ site.baseurl }}/assets/images/waiting-for-vm-to-spin-up-from-dashboard-1024x459.png)

8\. Once ready select on it to see the overview and the IP address. Should look like this: ![vm-overview-ip]({{ site.baseurl }}/assets/images/vm-overview-ip-1024x583.png)

Great! We have a VM and its IP address. Lets use our Private SSH key to connect.

**C. Connect to VM using SSH Keys**

1\. Open bash to file location you created the keys in. Make sure they're there: `$ ls | grep server`

2\. Enter this command to use SSH to connect: `$ ssh -i server-key Ubuntu@52.183.31.11 -v` or more generally `$ ssh -i keyname username@ip.address -v` Make sure you're using server-key and not server-key.pub Tip: -v is the verbose option. Not necessary, but it helps to see if the key is being accepted

3\. Great, now accept the certificate, and enter your memeroablePassphrase Whole thing should look like this: ![ssh-using-key-to-inbash]({{ site.baseurl }}/assets/images/ssh-using-key-to-inbash-1024x200.png)

And you'll be in the terminal of your VM: ![in-the-terminal-of-the-vm]({{ site.baseurl }}/assets/images/in-the-terminal-of-the-vm-1024x235.png)

Yay! You've got the key, you've got the VM, now put it to work! [Flask on Ubuntu](http://timmyreilly.azurewebsites.net/running-flask-on-ubuntu-vm/) [Node on Ubuntu](http://timmyreilly.azurewebsites.net/running-node-and-express-on-ubuntu-vm/) [Mongo on Ubuntu](http://timmyreilly.azurewebsites.net/running-mongo-on-ubuntu-virtual-machine-in-azure/) [Connecting to VMs from Azure Web Apps](http://timmyreilly.azurewebsites.net/running-mongo-on-ubuntu-virtual-machine-in-azure/)

Let me know if you have any questions by posting in the comments below!

\[caption id="attachment\_9301" align="aligncenter" width="4032"\]![These people just want High Fives! ]({{ site.baseurl }}/assets/images/reactor-hacker-photo.jpg) These people just want High Fives!\[/caption\]

