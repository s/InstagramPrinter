InstagramPrinter
================

A Python application that searchs and prints Instagram photos with the given hashtag.

Edit the <code>Api.py</code> class' members: <code>searchHashtag</code> and <code>accessToken</code>

Quickly run the command: <code>python App.py</code>

![Command Line Screen Shot](https://raw.github.com/saidozcan/InstagramPrinter/master/screenshots/terminal.png)

![View Screen Shot](https://raw.github.com/saidozcan/InstagramPrinter/master/screenshots/view.png)

Generated html files will be stored in <code>/output/views/</code>

View Template Tags:

{$title}                    : Page Title
{$photoUrl}                 : Url of photo
{$photoWidth}               : Width of photo
{$photoHeight}              : Height of photo
{$postOwnerAvatar}          : Avatar of post owner
{$postOwner}                : Screen username of post owner
{$postDate}                 : Create date of post
{$likes}                    : People who likes this post
{$comments} .. {/$comments} : Comments block
{$commentOwnerAvatar}       : Avatar of owner of any comment
{$commentOwner}             : Screen username of owner of any comment
{$commentText}              : Text of comment
