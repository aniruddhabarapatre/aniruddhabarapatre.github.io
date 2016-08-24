---
title: Convert binary data to image in ColdFusion
date: 2015-06-20 23:42 EDT
tags: ColdFusion
Category: Blog
---

Converting binary data to any image format has been made pretty easy in ColdFusion

    <cfset myImage = ImageReadBase64("data:image/jpg;base64,#toBase64(binaryPhoto)#")>

As above, binary data first has to be converted to base 64 using method `tobase64`, which can be further converted to required format using ColdFusion supported method `ImageReadBase64`.
