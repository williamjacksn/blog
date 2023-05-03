title: A Note About Gmail Contacts
urlname: gmail-contacts
date: 2006-08-12T08:39

Overall, I really enjoy using the Gmail interface; but there is one thing that bothers me to no end, that probably shouldn&#x02bc;t bother me to no end. There is a single difference in the way contacts are displayed when you are using Microsoft [Internet Explorer](http://www.microsoft.com/windows/ie/ie6/default.mspx) and Mozilla [Firefox](http://www.mozilla.com/firefox/).

I use Firefox the most, so we&#x02bc;ll start with it. Here&#x02bc;s a clip from the contact list showing a contact and a group:

![Gmail contact list in Firefox](https://dl.dropboxusercontent.com/s/vdrwf2q32j10qbf/20060812-gmail-contacts-ff.png)

The only difference between the display of a contact and a group is that for a contact, the actual email address is shown, and for a group, the number of contacts in the group is shown.

Now take a look at the same clip in Internet Explorer:

![Gmail contact list in Internet Explorer](https://dl.dropboxusercontent.com/s/fv5pr4j6rarv6wi/20060812-gmail-contacts-ie.png)

The big difference I am pointing out here is that group names are bold and contact names are not.

I like the contact list display in Internet Explorer more, and it _feels_ to me like this is the &ldquo;correct&rdquo; way, but alas: when I view the page source (in Firefox), I can see that there is an explicit `&lt;b&gt;` tag surrounding the names. So they are _supposed_ to be bolded, and Internet Explorer just isn&#x02bc;t doing what it is asked to do.

Also, Internet Explorer won&#x02bc;t let me see the page source. When I right-click on the page and choose __View Source__, nothing happens. When I choose __Source__ from the __View__ menu, &hellip; nothing happens.

Interestingly, when I switch to basic HTML view, all the contact names are bolded in both browsers, but the contact groups disappear.