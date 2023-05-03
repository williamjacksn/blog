title: I learned another incantation
urlname: another-incantation
date: 2008-01-29T10:37

A few months ago I purchased a computer. For the first time in my life. It is a new-to-me [Apple PowerBook G4](http://support.apple.com/kb/SP48) I bought off the son of a coworker of Rebecca. I have used Apple&#x02bc;s Mac OS X quite a bit at school and always preferred it to my Windows XP (and my [Linux](http://www.ubuntu.com/ubuntu)!), but Apple computers are expensive. So I got a good deal, and bought it, and have experienced no remorse whatsoever.

Now with my job I have been supporting some Apple computers rather closely, and learning so much more about the operating system, specifically how I can configure just about anything with the Terminal. You know, type type type? Text-only? _UNIX_? It really is great.

In a way, learning and using Linux (i.e. UNIX (i.e. [POSIX](http://en.wikipedia.org/wiki/POSIX))) for my server has prepared me for Mac OS X and helped me to appreciate it more.

Also, there is remote administration. I can see the computers without leaving my desk. I can control them, even if someone else is logged in and using them. That would probably be a bit freaky: you&#x02bc;re mousing around when suddenly, the mouse is moving on its own and there is nothing you can do about it.

I haven&#x02bc;t tried that on anyone yet.

Here is the problem I ran into, however: I want to change a setting, but to do so I need to take control of the computer and open System Preferences, &amp;c. I don&#x02bc;t want to interrupt the user to do it. I was considering this, when I remembered all the times I read tips online for configuring Mac OS X before I actually owned such a computer, and I remembered that the tip-giver would almost always give a Terminal command to effect the change, and said Terminal command would almost always begin with `defaults`.

So, I did some digging and learned about the `defaults` command, and, long story short (&ldquo;Too late!&rdquo;), I came up with these magic words:

```defaults delete /Library/Preferences/com.apple.loginwindow PowerOffDisabled
```

This command shows the Restart and Shutdown buttons on the login window (so you can turn off the computer without logging in first). Having a Terminal command to do this is great because I can run such commands on the computers I administer without interrupting the current user. All behind the scenes. It is very clever.