InstagramPrinter
================

A Python application that searchs and prints(soon) Instagram photos with the given hashtag.

Application first connects to Instagram Api and fetchs matched photo datas.<br/>

Then clones the template <code>main.html</code> and replaces tags with returning data from Api.

##Installation and Run

```
$ git clone git://github.com/s/InstagramPrinter.git ~/InstagramPrinter
$ cd ~/InstagramPrinter
$ python app.py
```


##Skeletal
  <h3>Classes: (Core python files)</h3><br/>
    <code>Api.py</code> : Handles Instagram Api connection and generates html files.<br/>
    <code>Printer.py</code> : Prints generated html files with connected printer.<br/>
  
   <h3>Output: (Public data)</h3><br/>
    <code>assets</code>          : Contains css and font files.<br/>
    <code>templates</code>        : Contains original templates.<br/>
    <code>views</code>           : Contains generated views. Generated views will be in the folder for e.g <code>views/#InstagramPrinter</code><br/>

##Configuration (config.yaml)  
  <code>accessToken      </code>  : Instagram api access token.<br/>
	<code>searchHashtag    </code>  : Hashtag to search. Default:<code>InstagramPrinter</code><br/>	
	<code>delayTime        </code>  : Delay time between each api request. Default: <code>30</code>(seconds)<br/>	
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
