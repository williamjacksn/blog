title: Putting Outlook Email Messages in Gmail
urlname: outlook-gmail
date: 2006-02-14T16:25

I like [Gmail][a]. I like the idea of never throwing away email messages. But before I had Gmail, I was already hoarding
email. I&#x02bc;ve been keeping my messages in archives since 2001.

[a]: https://www.google.com/gmail/about/

Ideally, I wanted to get these messages into Gmail, so I could search for them just like all my other messages. This is
how I did it.

__These are the steps I took to get _email messages only_ from Microsoft Outlook `.pst` files into Gmail.__

Here&#x02bc;s what you need:

1.  Microsoft Outlook. I&#x02bc;ve been using Outlook for years, so all my email was stored in Microsoft&#x02bc;s `.pst`
    format. It works really well for offline storage, as long as you have a copy of Outlook to read the files.
2.  [Mozilla Thunderbird][b]. If you are not aware, Thunderbird is an email client like Microsoft Outlook, but it stores
    email in a different format. It uses something called `mbox` format, which is a standard across most email programs
    (except Microsoft&#x02bc;s of course). The latest version of Thunderbird can import messages from Outlook.
3.  [Mark Lyon&#x02bc;s Google GMail Loader][c]. GML is the program that actually transfers the email messages from your
    computer to Gmail. It doesn&#x02bc;t understand `.pst` files (yet), so that&#x02bc;s why we need Thunderbird: to get
    the messages into `mbox` format.
    
[b]: https://www.thunderbird.net/en-US/
[c]: https://marklyon.org/2013/01/gmail-loader/

Here&#x02bc;s what you do:

1.  Make sure Outlook is installed correctly.
2.  For simplicity, move all your messages into the Inbox or Sent Items of your Personal Folders. If your messages are
    in an external `.pst` file, open it using File &rarr; Open &rarr; Outlook Data File&hellip;
3.  Exit Outlook. Install Thunderbird.
4.  When you run Thunderbird for the first time, it will ask you about importing stuff from other programs. Choose
    Outlook from the list and click Next. If you had a lot of messages, this will take a while. Click Finish when you
    get the chance.
5.  Check the folders in Thunderbird to make sure your messages really made it in. Exit Thunderbird. You&#x02bc;re
    almost done.
6.  Download, extract and run the GMail Loader program (gmlw.exe). Click the Find button and go digging for
    Thunderbird&#x02bc;s mail files. The default location is:

    `C:\\Documents and Settings\\&lt;username&gt;\\Application Data\\Thunderbird\\Profiles\\Mail\\Local Folders\\`
    
    For each folder in Thunderbird, there are two files in that directory. One ends in `.msf`, and the other
    doesn&#x02bc;t have an extension. Select the one without the extension.
7.  In GML, set the File Type to &ldquo;mBox (Less Strict - Solves Some Problems)&rdquo;. Set the message type according
    to your preference. If you are uploading files that you sent, choose, obviously, &ldquo;Mail I Sent (Goes to Sent
    Mail)&rdquo;. If it&#x02bc;s mail from other people to you, pick the other option.
8.  Enter your Gmail address and click &ldquo;Send To GMail&rdquo;. Then wait.
    
When the messages show up in your Gmail inbox, they won&#x02bc;t be threaded properly, but they will be there and
searchable. And with Gmail, that&#x02bc;s what really counts.
