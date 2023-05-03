title: In Which the Author Attempts to Explain C S
urlname: explain-cs
date: 2004-08-04T04:44

I just spent the last hour researching and writing code. Because I am only a beginning programmer, I _always_ research before (and during) my code-writing. I don&#x02bc;t know enough to just sit down and peck out the next great cross-platform application in an hour.

However, I _do_ know how to use [Google](http://www.google.com/). Here are the results.

Any respectable weblog application ([Movable Type](http://www.sixapart.com/movabletype/), [LiveJournal](http://www.livejournal.com/), [Blogger](http://www.blogger.com/start), [WordPress](http://wordpress.org), and [all the rest](http://www.intertwingly.net/wiki/pie/RoadMap#head-8aa335e17d48d61829f9234ebad88bccf402b6a4)) has something called an application programming interface, or API. The API makes up the list of commands and instructions that the application understands and will respond to. If you try to give an application an instruction that is not listed in its API, the poor app will just look at you and do one of two things: spin around in confusion for several minutes while hinting at imminent explosion; or laugh uncontrollably at you. The API outlines the language that the application speaks.

Fortunately, most weblog applications have similar APIs. For example, Blogger and Movable Type will recognize most of the same instructions (LiveJournal is on its own on this one). Hence, all one needs to do is learn the language an application speaks, and one has power to control the aforementioned application.

But the actual physical computer that the application is running on is over there (waves hand in general direction of cyberspace, perhaps to the east), and the computer that I am using right now is right here. How can I talk to the application over there? In the weblog situation, which is what I am focusing on at the moment, there is already a framework set up for communication between computers. We call it the Internet.

Instructions are sent to the application in a format called extensible markup language, or XML. This format is an Internet standard that conforms to certain rules which I will not explain here.

If one is trying to talk to an application through its API, one is most likely trying to get the application to _do_ something, to follow a certain procedure. When one tells an application to do something, one makes what is referred to as a remote procedure call, or RPC. The general term for the language that an application understands when sent an instruction over the Internet is XML-RPC API.

So, using Google along the way, I wrote a program in Java that creates a document that conforms to both the XML standard and the API language of the weblog application of my choice (in this case, Movable Type). The program then opens a connection to the computer where the application is running, then sends the document and waits for a response. When the response comes, the program creates a file on my local hard disk that contains the response that came from the remote computer.

The only thing my first program does is request a list of entry titles.

To tell you the truth, this sort of thing really excites me. I guess you could tell that from the fact that this is the longest entry I have ever written. It probably took me longer to write this post than it did to write the program.

Whoa, this _is_ a long post. I suppose it&#x02bc;s more for my benefit than anyone else. Well, if you make it this far, congratulations and have a wonderful day!