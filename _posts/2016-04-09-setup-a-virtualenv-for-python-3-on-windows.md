---
title: "Setup a virtualenv for Python 3 on Windows"
date: "2016-04-09"
tags: 
  - "command"
  - "delete"
  - "mkvirtualenv"
  - "prompt"
  - "python"
  - "python35"
  - "rmvirtualenv"
  - "three"
  - "virtualenv"
  - "virtualenv-win"
  - "windows"
  - "workon"
---

It's essentially the same as Unix!

Especially, if you've followed my other guide to getting setup virtualenvs and virtualenvwrapper-win on Windows. And you've also installed python3!

Here's the Script I run: `mkvirtualenv --python=C:\Python35-32\python.exe pythonthreeEnv`

'pythonthreeEnv' is the name of my environment.

Now I can run: `workon pythonthreeEnv`

Here's a screenshot of a workflow: ![pythonthreeenv]({{ site.baseurl }}/assets/images/pythonthreeenv.png)

Bonus: To efficiently delete an env: `rmvirtualenv pythonthreeEnv -r`

Happy Hacking!

\[caption id="attachment\_7101" align="aligncenter" width="4032"\]![THESE THINGS ARE AMAING. Thank you Alejandro and Argentina!]({{ site.baseurl }}/assets/images/IMG_20160409_0103141.jpg) THESE THINGS ARE AMAZING. Thank you Alejandro and Argentina!\[/caption\]

