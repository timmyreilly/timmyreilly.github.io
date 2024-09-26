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
