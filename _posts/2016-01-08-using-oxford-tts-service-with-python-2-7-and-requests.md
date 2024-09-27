---
title: "Using Oxford TTS Service with Python 2.7 and Requests"
date: "2016-01-08"
---

This is a follow up to a recent post I made about using [Project Oxford with Python](http://timmyreilly.azurewebsites.net/python-flask-text-to-speech-tts-microsoft-project-oxford/). If you haven't used Project Oxford before visit that post and complete the first three steps to acquire a token.

The previous example used Python 3 and [urllib](https://docs.python.org/3.5/library/urllib.html) which is cool. But I'm more familiar with the [requests](http://docs.python-requests.org/en/latest/) library and python 2 so I spent some time re-writing the app with requests, and in the process learned what's actually going on.

The source code can be found here: [https://github.com/timmyreilly/oxford-tts-requests.](https://github.com/timmyreilly/oxford-tts-requests.)

And the example from the Project Oxford Official Repo for python 3 can be found here: [https://github.com/Microsoft/ProjectOxford-ClientSDK/blob/master/Speech/TextToSpeech/Samples-Http/Python/TTSSample.py](https://github.com/Microsoft/ProjectOxford-ClientSDK/blob/master/Speech/TextToSpeech/Samples-Http/Python/TTSSample.py)

The meat of the program is tts.py which provides the methods we use in the app to provide an access token and use it to hit the API with our words to digitize.

Here's a link to it if you'd like to follow along: [https://github.com/timmyreilly/oxford-tts-requests/blob/master/FlaskWebProject/tts.py](https://github.com/timmyreilly/oxford-tts-requests/blob/master/FlaskWebProject/tts.py)

Then we take that token and send a POST request with our access Token and specific headers "TTS\_HEADERS" and "body" which includes the text to be translated.

After we POST we receive a JSON object that we encode into base 64 and inject into our HTML Template (index.html) using views.py.

To run this project: `clone the project create a virtual env pip install requirements.txt python runserver.py visit http://localhost:5555/`

This project is ready to be deployed to Azure as a Web App! If you don't know/care about that you can simply delete all the other files besides runserver.py and the contents of FlaskWebProject

Let me know if you have any questions or would like to contribute to the next iteration!

\[caption id="attachment\_6611" align="aligncenter" width="4032"\]![What's underneath the Man suit? ]({{ site.baseurl }}/assets/images/IMG_20160102_144146.jpg) What's underneath the Man suit? \[/caption\]

