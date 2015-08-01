WebXploiter V0.1
================
This is a basic version of WebXploiter. As of now, it will do a basic Recon and print the results back.

Install:
-------
Just run `python install.py` from install directory. Rest is taken care of :) 

Usage:
------
```
WebXploit.py [-h] [-u U] [-o O]

Do a basic Recon for Web challenges

optional arguments:
  -h, --help    show this help message and exit
  -u U, -url U  Target URL to Recon
  -o O, -out O  Filename to save output
````

Sample Output:
--------------
A sample output against localhost:

```
python WebXploit.py -u http://localhost/challs/action.php

m     m        #      m    m        ""#             "      m
#  #  #  mmm   #mmm    #  #  mmmm     #     mmm   mmm    mm#mm
" #"# # #"  #  #" "#    ##   #" "#    #    #" "#    #      #
 ## ##" #""""  #   #   m""m  #   #    #    #   #    #      #            """  
 #   #  "#mm"  ##m#"  m"  "m ##m#"    "mm  "#m#"  mm#mm    "mm
                             #
                             "

        mmmmm
        #   "#  mmm    mmm    mmm   m mm
        #mmmm" #"  #  #"  "  #" "#  #"  #
        #   "m #""""  #      #   #  #   #
        #    " "#mm"  "#mm"  "#m#"  #   #


===============================================================
Response Headers:

x-powered-by           : PHP/5.5.9-1ubuntu4.11
set-cookie             : PHPSESID=This+is+your+cookie, lol=this+is+another+test
keep-alive             : timeout=5, max=100
server                 : Apache/2.4.7 (Ubuntu)
connection             : Keep-Alive
date                   : Thu, 30 Jul 2015 11:51:16 GMT
content-type           : text/html
===============================================================
Cookies:

PHPSESID               : This+is+your+cookie
lol                    : this+is+another+test
===============================================================
Robots.txt Analysis:

test
```
Contribute:
-----------

If you have any feature requests or came across any bugs, do add a new [issue](https://github.com/a0xnirudh/bi0s-CTF-Scripts/issues) or give a pull request ;)
