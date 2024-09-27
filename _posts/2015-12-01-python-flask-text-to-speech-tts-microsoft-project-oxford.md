---
title: "Python, Flask, Text to Speech (TTS), Microsoft, Project Oxford!"
date: "2015-12-01"
---

Microsoft Provides at TTS service API to help hackers bring voice to their applications.

This is an introduction to the technology as well as working sample code for Python34.

Two weeks ago I worked with a number of students to use this service in a Python Web App. Here's some photos of the guys I worked with:

![hackschackers]({{ site.baseurl }}/assets/images/IMG_20151115_041036.jpg)

![hackucihackers]({{ site.baseurl }}/assets/images/IMG_20151121_224450.jpg)

If you're already familiar with Project Oxford feel free to skip the first 3 steps.

It seems like some of the API services are being moved from Bing to under [Project Oxford](https://www.projectoxford.ai) so some of the documentation can be a bit scattered.

I want to point you into the simplest path to make this happen and help trim off some of the overhead that might look daunting at first.

**1.** We'll start at the Project [Oxford Speech API landing page.](https://www.projectoxford.ai/speech)

![signinsubscribe]({{ site.baseurl }}/assets/images/signinsubscribe.png)

**2.** Then sign in and subscribe:

You can also look at the live demos/documentation to get started and test the capabilities.

![mykeys]({{ site.baseurl }}/assets/images/mykeys.png)

**3.** Now that we're signed up and have access to our keys go ahead and keep that tab open because you'll need to use you're own key to get this sample code working.

**4.** In the meantime there is some important documentation to read over to help familiarize yourself with what's going on: (Reminder - this API is still in Beta so expect changes along the way)

[First is the overview of the Bing Voice Output API](https://www.projectoxford.ai/doc/speech/REST/Output) Make sure to check out all the available voices!

[And this is the code that we turned into a tiny flask app](https://github.com/Microsoft/ProjectOxford-ClientSDK/blob/master/Speech/TextToSpeech/Samples-Http/Python/TTSSample.py)

**5.** Two things that I found most confusing about using this sample code...

What is the clientID? And What the heck do you do with the data you get back?

**6.** So here's the code we wrote: Its a tiny flask web app. Here's a link to the repository: [https://github.com/timmyreilly/tiny-tts-flask](https://github.com/timmyreilly/tiny-tts-flask)

to run on my machine I execute:

`C:\Python34\python.exe app.py`

...Because I have Python 2.7 and Python 3.4 on my machine I run it from C:\\

**7.** The clientID doesn't need to be anything... I found out. So you'll see at [line 13 in the helper.py file](https://github.com/timmyreilly/tiny-tts-flask/blob/master/helper.py) client\_id is set to 'nothing'

**8.** Now what to do with the data you get back...

Well it turns out you can request all sorts of different formats.

You'll see in the headers declaration of helpers.py

`"X-Microsoft-OutputFormat": "riff-8khz-8bit-mono-mulaw",`

We're requesting a specific file type in return with this header and you can set it to a number of different formats.

You'll see at this documentation all the different available formats: https://www.projectoxford.ai/doc/speech/REST/Output

we changed our format from the mono-pcm to mulaw -> which has to do with audio compression.

Basically we get back a string that we can encode into base 64 trim the edges and send raw to the browser which will be available to play with the audio tag.

You'll see this at line 46 of helper.py with our get\_raw\_wav function.

**Note:** The body of our request can be edited to get different voices (male/female) different languages, and even different cadences.

This all falls under the Speech Synthesis Markup Language (SSML) you can read more about here: [http://www.w3.org/TR/speech-synthesis/](http://www.w3.org/TR/speech-synthesis/) and how Microsoft uses it here: [https://msdn.microsoft.com/en-us/library/hh361578(v=office.14).aspx](https://msdn.microsoft.com/en-us/library/hh361578(v=office.14).aspx)

Let me know if you have any questions! Feel free to submit a pull request or fork this code for your next hackathon!

\[caption id="attachment\_6391" align="aligncenter" width="3024"\]![Happy Thanksgiving massive tree on the panhandle!]({{ site.baseurl }}/assets/images/IMG_20151127_164504.jpg) Happy Thanksgiving massive tree on the panhandle!\[/caption\]

