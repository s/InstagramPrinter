InstagramPrinter
================

A Python application that searchs and prints Instagram photos with the given hashtag.

##Run

Quickly type the command: <code>python App.py</code> in the folder that includes <code>App.py</code>.


##Skeletal
  ###Classes:Core python files<br/>
    <code>App.py</code> : Application runner file.
    <code>Api.py</code> : Handles Instagram Api connection and generates html files.
    <code>Printer.py</code> : Prints generated html files with connected printer.
  
  ###Output:Views-Templates-Assets<br/>
    ####assets          : Contains css and font files.
    ####templets        : Contains original templates.
    ####views           : Contains generated views.

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

Generated html files will be stored in <code>/output/views/</code>

