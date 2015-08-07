WebXploiter V0.1
================
This is a basic version of WebXploiter. As of now, it will do a basic Recon and print the results back.

Install:
-------
Just run `python install.py` from install directory. Rest is taken care of :)

Usage:
------
```
usage: WebXploiter.py [-h] [-u U] [-a] [-A1] [-A3]

Do a basic Recon for Web challenges

optional arguments:
  -h, --help    show this help message and exit
  -u U, -url U  Target URL to Recon
  -a, -all      Try all possible attacks
  -A1           Test for only Injection Attacks
  -A3           Test for only XSS Attacks

````

Sample Output:
--------------
A sample output against localhost:

```
python WebXploiter.py -u "http://localhost/challs/action.php" -a

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
set-cookie             : lol=bG9sCg%3D%3D, PHPSESID=44705989020
keep-alive             : timeout=5, max=100
server                 : Apache/2.4.7 (Ubuntu)
connection             : Keep-Alive
date                   : Fri, 07 Aug 2015 18:13:27 GMT
content-type           : text/html
===============================================================
Robots.txt Analysis:

test

===============================================================
Cookies:

PHPSESID               : 20639818163
lol                    : bG9sCg%3D%3D

Base64 Encoded Cookies: (Attention!)
lol                    : lol

=======================================================
Possible Attack:

POC: lol: bG9sCg%3D%3D'
Error Based SQL Injection (Cookie Based)
Refer: https://www.exploit-db.com/docs/33253.pdf

=======================================================
Possible Attack:

Error Based SQL Injection (User-Agent)
POC: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'

Refer: http://resources.infosecinstitute.com/sql-injection-http-headers/
```
Contribute:
-----------

If you have any feature requests or came across any bugs, do add a new [issue](https://github.com/team-bi0s/WebXploiter/issues) or give a pull request ;)
