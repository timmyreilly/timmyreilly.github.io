

```
bundle install
bundle exec jekyll serve
```





# Archive. Prompts

## old image location

https://github.com/timmyreilly/blog_backup/tree/main/blog/_posts/images


## Pormpt for converting blogs



I need to update a number of files, they all are a little bit different, but I know we can straighten them out with some code. 

Here is what they look like before conversion: 

```
---
layout: post
title: "AT&T MMS Issues FIXED"
date: "2014-11-21"
tags: 
  - "1320"
  - "apn"
  - "content"
  - "download"
  - "in"
  - "media"
  - "message"
  - "mms"
  - "mmsc"
  - "nokia"
  - "proxy"
---

One awesome thing about windows phone is the wide array of commodity phones.

I love the reliability and durability of Nokia and they are pricing phones at ~$50 bucks OFF CONTRACT!

So, essentially you could have a different phone everyday.

It just so happens that some of these phones are only available in non-us markets.

I purchased the [Nokia 1320](http://www.microsoft.com/en/mobile/phone/lumia1320/ "Microsoft Site"), but it wasn't configured to pick up MMS messages from AT&T and I found a fix.

As of November 2014 this is what works for me.

1\. Settings > cellular+SIM

2\. Make sure active network is AT&T and Data Connection is toggled On

3\. Tap on SIM settings

4\. You can make the SIM name whatever you want

5\. Select the highest connection speed

6\. Network Selection > Automatic

7\. Manual Internet APN > On

8\. Tap 'edit internet APN'

9\. Form should read like this: ( \_\_\_ is blank )

APN: pta User name: \_\_\_ Password: \_\_\_ Authentication Type: PAP Proxy Server(URL): \_\_\_ Proxy port: \_\_\_ IP type: IPv4

9\. Tap the Save Icon at the bottom

10\. Tap 'edit MMS APN'

11\. Form should read like this: ( \_\_\_ is blank )

APN: pta User Name: \_\_\_ Password: \_\_\_ Authentication type: PAP WAP gateway (URL): proxy.mobile.att.net WAP gateway port: 80 MMSC (URL): http://mmsc.mobile.att.net/ MMSC port: 80 Maximum MMS size: 1 IP type: IPv4

12\. Tap the Save Icon.

13\. Go back and tap on any messages that say "Get media content now (1kb)" to download those missing messages.

\[caption id="attachment\_2291" align="aligncenter" width="474"\]![Ciaran y Andrew son atractivas ](images/IMAG0023-685x1024.jpg) Ciaran y Andrew son atractivas \[/caption\]

I'll be switching phones again soon, so if I need to make any other adjustments I'll post again.
```

And this is what they need ot look like after:

```
---
layout: post
title: "AT&T MMS Issues FIXED"
date: "2014-11-21"
tags: 
  - "1320"
  - "apn"
  - "content"
  - "download"
  - "in"
  - "media"
  - "message"
  - "mms"
  - "mmsc"
  - "nokia"
  - "proxy"
---

One awesome thing about windows phone is the wide array of commodity phones.

I love the reliability and durability of Nokia and they are pricing phones at ~$50 bucks OFF CONTRACT!

So, essentially you could have a different phone everyday.

It just so happens that some of these phones are only available in non-us markets.

I purchased the [Nokia 1320](http://www.microsoft.com/en/mobile/phone/lumia1320/ "Microsoft Site"), but it wasn't configured to pick up MMS messages from AT&T and I found a fix.

As of November 2014 this is what works for me.

1\. Settings > cellular+SIM

2\. Make sure active network is AT&T and Data Connection is toggled On

3\. Tap on SIM settings

4\. You can make the SIM name whatever you want

5\. Select the highest connection speed

6\. Network Selection > Automatic

7\. Manual Internet APN > On

8\. Tap 'edit internet APN'

9\. Form should read like this: ( \_\_\_ is blank )

APN: pta User name: \_\_\_ Password: \_\_\_ Authentication Type: PAP Proxy Server(URL): \_\_\_ Proxy port: \_\_\_ IP type: IPv4

9\. Tap the Save Icon at the bottom

10\. Tap 'edit MMS APN'

11\. Form should read like this: ( \_\_\_ is blank )

APN: pta User Name: \_\_\_ Password: \_\_\_ Authentication type: PAP WAP gateway (URL): proxy.mobile.att.net WAP gateway port: 80 MMSC (URL): http://mmsc.mobile.att.net/ MMSC port: 80 Maximum MMS size: 1 IP type: IPv4

12\. Tap the Save Icon.

13\. Go back and tap on any messages that say "Get media content now (1kb)" to download those missing messages.

![Ciaran y Andrew son atractivas]({{ site.baseurl }}/assets/images/IMAG0023.jpg)

I'll be switching phones again soon, so if I need to make any other adjustments I'll post again.

```

Please write the code to convert the files, you can start with this one, note the change in the file path: 

```
---
title: "Back on the Train"
date: "2014-08-12"
---

I'm happy to be writing again. I had taken a couple week break to get settled and determine if continuing this blog was in line with my new "Professional Career." Turns out it is!

\[caption id="attachment\_294" align="alignnone" width="474"\][![Desk](images/IMG-20140804-WA0000-768x1024.jpeg)](http://timmyreilly.azurewebsites.net/wp-content/uploads/2014/08/IMG-20140804-WA0000.jpeg) My Very Professional Desk! \[/caption\]

I started my role as a Technical Evangelist at Microsoft on July 7th, and will be contributing to this blog weekly; blurring the lines between professional evangelist and unprofessional man of many curiosities.

If you have any questions about Windows development or being a man, please don't hesitate to ask!

Today on the agenda, is practicing presentation skills. One of our many mentors, John Alioto, has given us a couple of topics to research and use as material for our 5 minute talk. The questions are really good, I can't share them with you now, but when I get the okay they are all worth investigating.

Ahhhh good question John. Taking us back to compilers... We'll get to the full rundown later this week.

\[caption id="attachment\_293" align="alignnone" width="474"\][![The Moon](images/IMG_20140807_224627-1024x768.jpg)](http://timmyreilly.azurewebsites.net/wp-content/uploads/2014/08/IMG_20140807_224627.jpg) I took this photo at the Oregon Observatory in Sunriver through one of the many beautiful telescopes you can use for just $8! \[/caption\]

```



Okay, that might have been overkill to write the code, can you just convert this one and just provided it directly? 



## 

