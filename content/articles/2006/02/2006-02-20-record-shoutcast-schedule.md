title: How to Record a Shoutcast Stream on a Schedule
urlname: record-shoutcast-schedule
date: 2006-02-20T08:36

Have you heard? I&#x02bc;ve been drumming up _Labarum for the Latter Day_ for a while. But stuff keeps coming up and I
miss it. I decided that I need to record the broadcasts automatically. This is how I did it.

This process can be generalized to record any shoutcast-compatible audio stream. Because of the nature of this
operation, it is well-suited to be done on a server that is always running.

Here&#x02bc;s what you need:

1.  Unix, on a computer with internet access that is turned on (of course) at the time you want to record the stream.
    Servers work great. These instructions assume you have command-line access to your server.
2.  Perl. Most Unix computers have Perl installed already. Type `which perl` to find out if you have Perl installed on
    your server.
3.  `cron`. If you have Unix and you don&#x02bc;t have `cron`, something is wrong with you. `cron` is the program that
    runs other programs on a particular schedule. Other programs like &hellip;
4.  [icecream][a]. No, really, `icecream` is the Perl script that does all the work. It wouldn&#x02bc;t hurt to have
    some vanilla ice cream handy, too.

[a]: https://icecream.sourceforge.net/

Here&#x02bc;s what you do:

1.  Download `icecream`. Unzip the files and put them on your server somewhere. I put mine in `/home/william/icecream/`
2.  Set up `cron` to run `icecream` when you need to. Type `crontab -e` to edit your `cron` jobs. On a new line in the
    crontab file, follow the [crontab format][b] to specify when you want the job to run. Here&#x02bc;s what I used:

    `25 19 \* \* 3 perl /home/william/icecream/icecream -q --name=kvrx-\\%Y-\\%m-\\%d --stop=40min
    http://129.116.109.132/listen.pls`
    
    `25 19 \* \* 3` means the command will be executed at 7:25pm on the third day of every week.
    
    `perl /home/william/icecream/icecream` is the actual command to run `icecream`.
    
    `-q` tells `icecream` to not output anything (q is for quiet).
    
    `--name=kvrx-\\%Y-\\%m-\\%d` gives the name of the file `icecream` will create when it records the radio stream.
    `%Y-%m-%d` gives the current date, while the backslashes are there to keep `cron` from complaining. I learned that
    through trial and error.
    
    `--stop=40min` tells `icecream` to stop recording after 40 minutes have passed.
    
    `http://129.116.109.132/listen.pls` is the location of the stream.
3.  Wait for the appointed time to come around, then look in your home directory for the file that `icecream` created.
    That&#x02bc;s all!
    
[b]: https://en.wikipedia.org/wiki/Cron    

I should never miss recording an episode of _Labarum for the Latter Day_ again.

Oh, and sorry. I know most of you hate reading or don&#x02bc;t read this sort of stuff, but I want to have it around in
case I need to do it again at some time in the future.
