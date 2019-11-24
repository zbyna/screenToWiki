# screenToWiki

This script enables to upload screenshot made by [ShareX´s](https://getsharex.com/) workflows to the media wiki site.

[Binary version](https://github.com/zbyna/screenToWiki/releases) of the script was created by [pyInstaller](https://www.pyinstaller.org/).

``` 
   Usage: screenToWiki.exe [OPTIONS] PATHTOFILE
   upload a file(picture) to MediaWiki site

   it is needed:

   1. site name e.g. http://192.168.1.13/wiki/api.php
   2. token for bot login -LOGIN_TOKEN
   3. login as a bot -  name, password
   4. token for upload  - CSRF_TOKEN
   5. upload image

Options:

  -s, --site-name TEXT
  -b, --bot-name TEXT
  -p, --password TEXT
  
  --help                Show this message and exit.
 ```

  
 e.g.```screenToWiki.exe pokus_obr.png -b User@user-bot -p k75ne0vbnei.....47arje07uo1o7 -s http://192.168.1.13/wiki/api.php ```

To use the script you need:



1. install amazing ShareX - of course :-)

	- taste what ShareX can [here](http://www.tangycode.com/ShareX-User-Manual/) thanks @AnacondaPython aka TangyCode

2. create media wiki bot for picture upload

![MediaWiki](https://i.imgur.com/EdBgabe.png)

3. create workflow in ShareX which includes the script

	- just duplicate 'Capture region' workflow 

	- set its Task properties
![Task properties](https://i.imgur.com/CIRSX3Q.png)
	- and Actions properties
![Actions properties](https://i.imgur.com/UsYsv2L.png)
	Args for example:
	``` %input -b User@user-bot -p k75n......rje07uo1o7 -s http://192.168.1.13/wiki/api.php ```
