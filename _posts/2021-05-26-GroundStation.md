---
layout: post
shortnews: true
icon: newspaper-o
image: '/img/UNLaMGroundStation.jpg'
image_style: "max-height: 200px;"
#image_link: "https://en.wikipedia.org/wiki/X-Men"
---
First step to close the cycle Engineering, from satellite to final applicacion. This week we had a success test of the new antenna. It was build in Argentina and works well with a Mini 70 amplifier. 
Using gpredict, gqrx and GNU Radio (helped by <a href="https://github.com/daniestevez/gr-satellites">gr-satellites</a>) we downloaded the bugsat1 (TITA) beacon directly from satellite. Finally we decoded audio successfully.
This is our first step to complete the cycle; from the satellite to final application,  <a href="https://ugs.unlam.edu.ar/#/browse/mine/demodash">Unlam Ground Segment</a>.   
We also planing to create a <a href="https://satnogs.org/">SatNogs</a> ground station soon!.  

This is the downloaded and decoded binary data:

***********************************
* MESSAGE DEBUG PRINT PDU VERBOSE *
((transmitter . 9k6 FSK downlink))
pdu_length = 109
contents = 
0000: 86 a2 40 40 40 40 60 98 aa 6e 82 82 00 e1 03 f0 
0010: 3a 45 4d 41 49 4c 20 20 20 20 3a 74 69 74 61 40 
0020: 73 61 74 65 6c 6c 6f 67 69 63 2e 63 6f 6d 20 00 
0030: 04 55 70 74 3a 20 30 34 3a 34 33 3a 31 34 20 01 
0040: 04 02 04 03 04 42 61 74 3a 31 31 2e 39 31 76 20 
0050: 04 04 54 65 6d 70 3a 32 34 2e 32 43 20 05 04 47 
0060: 79 72 3a 31 2e 34 30 64 2f 73 20 06 04 
***********************************