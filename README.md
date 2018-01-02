# Cherry solution brief  guide.

Cherry solution is composed of four sub projects:

![](https://raw.githubusercontent.com/Cherry-project/CherrySolution/master/ReadmePics/arhi.PNG)




## Genesis

#### Trivia
This project can be seen like a PHP web service containing some end-points. It is used to recieve HTTP requests from Project Poppy Core. The main part of this application is located in `\chatterbot23.php`. When an incoming request is recieved, `\chatterbot23.php` make use of `\AR.txt` and `\gen\*` files to interprete it and send back a text that should be said by ProjectPoppyCore.

#### Install

To install Genesis you need to have a PHP web server installed. You can use a pre-build packages like WAMP, it will work just fine. Make sure you know your web server&apos;s ip and http port, we&apos;ll use them later.
Place a `Genesis` folder into your web server&apos;s project location.
> Ex: C:/wamp64/www/Genesis

Now you should be able to access a web interface using your browser.
![](https://raw.githubusercontent.com/Cherry-project/CherrySolution/master/ReadmePics/genesis_web.PNG)

## CherryApp

#### Trivia
CherryApp is an Android application writen in JavaScript with help of three frameworks: Cordova, React and Ionic. This application communicates with Controller using HTTP requests.

#### Installation
For installation process please refer to this documentation: https://github.com/Cherry-project/wiki/wiki/App 

#### Configuration
In order to be integrated into Cherry Solution this application should know where Controller is located. Before building the apk go to `\www\js\app.js` and change the ip address (currently it&apos;s on line 19).  `$rootScope.cherryUrl` must point to your Controller.
>Ex: `$rootScope.cherryUrl="http://192.168.1.103:8080/";`


## Controller

#### Trivia

This is a java web service created with a spring framework. It should recieve requests from Android App and Poppy Core.

#### Installation

You can run this project inside an IDE. For this, import it into an IDE that supports Spring framework (Ex: Eclipse, IntelliJ).


## Project Poppy Core

Refer to this documentation for more details: https://github.com/Cherry-project/CherrySolution/blob/master/Proc%C3%A9dure%20controlleur%20poppy.docx 

#### Configuration

Make sure you have right ip in those locations:
- file ip.txt in `/home/poppy/resources/ip.txt` must contain ip address and port of your controller
- parameter `"server"` in `/projet_poppy_core/primitiveWS/cherry/config/conf.json` must contain ip address and port of your controller
- Variable `url` in `/projet_poppy_core/primitiveWS/cherry/chatterbot/chatterbot.py` must point to your Genesis. It will automatically pick up an ip address from ip.txt but you should manually set up the right port.
