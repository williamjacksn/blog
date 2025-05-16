title: Enabling postfix (sendmail) on Mac OS X 10.5 Leopard
urlname: enabling-postfix-sendmail-on-mac-os-x-10-5-leopard
date: 2009-06-21T17:58

I recently migrated off a web server running Ubuntu onto a server running Mac OS X 10.5 (client, not server). Everything
has been working except sending email. On Ubuntu, when someone left a comment on my blog, the web server sent me an
email. I hadn&#x02bc;t received any email from the server since I moved to OS X. Today I found out why.

Mac OS X 10.5 comes with a mail-sending program called `postfix`, but it is not turned on by default. Today, while
diagnosing the problem, I found [an excellent article explaining how to enable `postfix`][a] on OS X.

[a]: https://web.archive.org/web/20120603102344/http://pivotallabs.com/users/chad/blog/articles/507-enabling-the-postfix-mail-daemon-on-leopard

If you just want to send all of your outgoing mail to some relay server, like the SMTP server of your Internet service
provider, you usually need to have a host name for the computer that is sending the mail. This configuration is for a
server that is _not_ being used to receive mail.

Open __Terminal__ and enter the following commands, each on a single line. After the first command you will be prompted
for your password. (Oh, you need to be logged on as a user with administrative privileges.)

First, you want to set `postfix` to run when your computer tries to send mail:

```
% sudo launchctl unload /System/Library/LaunchDaemons/org.postfix.master.plist
% sudo defaults write /System/Library/LaunchDaemons/org.postfix.master OnDemand -bool true
% sudo launchctl load /System/Library/LaunchDaemons/org.postfix.master.plist
```

Next, you want to tell `postfix` what the host name of the computer is:

```
% sudo postconf -e myhostname=&lt;host-name-of-computer&gt;
```

Next, tell `postfix` what SMTP server to use to send email:

```
% sudo postconf -e relayhost=&lt;your-isps-smtp-server&gt;
```

This works for me because my ISP does not require authentication to use their SMTP server. They only require that the
traffic be coming from their network.

If the SMTP server you are using requires authentication, there are [a few extra steps][b]:

[b]: https://web.archive.org/web/20100123200709/https://www.freelock.com/kb/postfix-relayhost

```
% sudo echo &lt;you-isps-smtp-server&gt; &lt;username&gt;:&lt;password&gt; &gt;&gt; /etc/postfix/sasl_passwd
% sudo postconf -e smtp_sasl_auth_enable=yes
% sudo postconf -e smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd
```

At this point, if `postfix` tries to send email to `someone@&lt;host-name-of-computer&gt;`, the email will be delivered
locally. If your email for this host name is handled by some other server, tell `postfix` that this is not the final
destination for email sent to that host name:

```
% sudo postconf -e mydestination=localhost
```

I used the following specifically for my environment:

```
% sudo postconf -e myhostname=subtlecoolness.com
% sudo postconf -e relayhost=smtp-server.austin.rr.com
```

There! You should now be running `postfix` and your web server will send emails (again)!
