InstagramPrinter
================

A Python application that searchs and prints Instagram photos with the given hashtag.

Application first connects to Instagram Api and fetchs matched photo datas.<br/>

Then clones the template <code>main.html</code> and replaces tags with returning data from Api.

##Run

Quickly type the command: <code>python App.py</code> in the folder that includes <code>App.py</code>.


##Skeletal
  ## Classes: (Core python files)<br/>
    <code>App.py</code> : Application runner file.<br/>
    <code>Api.py</code> : Handles Instagram Api connection and generates html files.<br/>
    <code>Printer.py</code> : Prints generated html files with connected printer.<br/>
  
   <h2>Output: (Views-Templates-Assets)</h2><br/>
    ####assets          : Contains css and font files.<br/>
    ####templets        : Contains original templates.<br/>
    ####views           : Contains generated views.<br/>

##Api Class Members
  <code>apiUrl           </code>  : Instagram api url. Default: <code>api.instagram.com</code><br/>
  <code>accessToken      </code>  : Instagram api access token.<br/>
	<code>searchHashtag    </code>  : Hashtag to search. Default:<code>InstagramPrinter</code><br/>
	<code>method           </code>  : Instagram hashtag search api requires <code>GET</code> method.<br/>
	<code>apiPath          </code>  : Instagram api path. Default: <code>/v1/tags/HASHTAG/media/recent?access_token=ACCESSTOKEN</code><br/>
	<code>apiConnectionFlag</code>  : If there is a connection flag is 1. Default: <code>0</code><br/>
	<code>delayTime        </code>  : Delay time between each api request. Default: <code>30</code>(seconds) <br/>
	<code>outputDirectory  </code>  : Directory that contains generated html files. Default: <code>output/</code><br/>
	<code>pageTitle        </code>  : Page title of generated html file. Default: <code>InstagramPrinter</code><br/>

##View Template Tags:


<code>{$title}</code>                    : Page Title<br/>
<code>{$photoUrl}</code>                 : Url of photo<br/>
<code>{$photoWidth}</code>               : Width of photo<br/>
<code>{$photoHeight}</code>              : Height of photo<br/>
<code>{$postOwnerAvatar}</code>          : Avatar of post owner<br/>
<code>{$postOwner}</code>                : Screen username of post owner<br/>
<code>{$postDate}</code>                 : Create date of post<br/>
<code>{$likes}</code>                    : People who likes this post<br/>
<code>{$comments} .. {/$comments}</code> : Comments block<br/>
<code>{$commentOwnerAvatar}</code>       : Avatar of owner of any comment<br/>
<code>{$commentOwner}</code>             : Screen username of owner of any comment<br/>
<code>{$commentText}</code>              : Text of comment<br/>


##Screen Shots

![Command Line Screen Shot](https://raw.github.com/saidozcan/InstagramPrinter/master/screenshots/terminal.png)

![View Screen Shot](https://raw.github.com/saidozcan/InstagramPrinter/master/screenshots/view.png)
