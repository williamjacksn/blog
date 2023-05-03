title: On the Idempotence of Instagram Filters
urlname: instagram-filters
date: 2013-07-11T20:05

While I was recently posting a photo to Instagram, I had cause to wonder what would happen if I applied the same filter
to a photo multiple times. My wonder was caused by an interesting side effect of the app&#x02bc;s workflow on my phone.

The typical steps to take when posting to Instagram are these:

1.  Tap the &ldquo;take a photo&rdquo; button.
2.  Compose a photo and tap the shutter button to take the photo.
3.  Optionally apply a filter, border, and other effects to the photo.
4.  Optionally add a caption, tag people, add a location, and select social media sites to send the photo to.
5.  Upload to Instagram.

However, something happens behind the scenes between steps 3 and 4: the app saves a copy of the _edited_ photo to the
phone. I have found this useful in the past, particularly when I get to the captioning step and have to switch out of
the app to do something else. When I get back to the app I have often lost my work and need to compose a photo all over
again. But instead of taking a new photo (and editing it again) I can browse my phone and find the photo I edited the
first time.

At this point, the app does not know I just loaded a photo that the app itself created moments ago, so I get the option
to apply a filter and otherwise edit the photo again. So I began to wonder what would happen if I took advantage of this
to apply multiple filters to a photo.

### What Is Idempotence?

An operation is [_idempotent_][a] if it &ldquo;can be applied multiple times without changing the result beyond the
initial application.&rdquo;

[a]: https://en.wikipedia.org/wiki/Idempotence

So, an Instagram filter is idempotent if, after the first application, any subsequent application of the same filter
does not change the photo in any way. Applying the same filter several times is the same as applying the filter once.

My gut feeling is that Instagram filters are not idempotent, and if I apply a filter to the same photo over and over the
photo will look crazier and crazier. Let&#x02bc;s see if I am right.

### The Trilby

We&#x02bc;ll start with a boring photo of this fine trilby.

![Original photo, no filter applied.][b]

[b]: {static}/images/2013-07-11-ig-00.jpg

For this exercise I chose the Amaro filter. I liked how it helped bring out the pinstripes on the hat. Here is the
original photo with no filter (top-left), Amaro applied once (top-right), twice (bottom-left), and thrice
(bottom-right).

![Photo with no filter, then Amaro applied 1, 2, and 3 times.][c]

[c]: {static}/images/2013-07-11-ig-00-03.jpg

Already the photo is getting out of control. My hat is turning violet! And I was right, Amaro really brings out the
pinstripes. Also, the filters are not idempotent. But I kind of expected that anyway, I just needed an excuse to play
around with multiple filters!

But maybe after a few more applications of the filter, the photo will stabilize. Let&#x02bc;s keep going. Here is the
same photo with Amaro applied four, five, six, and seven times (top-left, top-right, bottom-left, bottom-right,
respectively).

![Photo with Amaro applied 4, 5, 6, and 7 times.][d]

[d]: {static}/images/2013-07-11-ig-04-07.jpg

There is still a fair bit of difference between Amaro &times;4 and Amaro &times;7. We&#x02bc;re giving up violet and
moving into the reds. What next?

![Photo with Amaro applied 8, 9, 10, and 11 times.][e]

[e]: {static}/images/2013-07-11-ig-08-11.jpg

The changes are slowing down now, but it is still easy to see differences.

![Photo with Amaro applied 12, 13, 14, and 15 times.][f]

[f]: {static}/images/2013-07-11-ig-12-15.jpg

Now we are all the way up to Amaro &times;15 (bottom-right). It is almost indistinguishable from Amaro &times;14.
We&#x02bc;ll stop here.

### All the Filters?

While we&#x02bc;re at it, how about one more crazy experiment before we&#x02bc;re through? What happens when _every_
filter is applied to a photo? Here is the original photo with filters applied cumulatively in this order: Amaro,
Mayfair, Rise, Hudson, Valencia, X-Pro II, Sierra, Willow, Lo-Fi, Earlybird, Sutro, Toaster, Brannan, Inkwell, Walden,
Hefe, Nashville, 1977, and Kelvin.

![Photo with all filters applied.][g]

[g]: {static}/images/2013-07-11-ig-allfilters.jpg

About halfway through we can still kind of tell it is a trilby, but by the time we get to the last four filters, who can
tell what that is a photo of? Nobody, that&#x02bc;s who.

Obviously, applying every filter at once is overkill and no one is going to do it. But we might get good results from
combining two or three filters. I wonder if the app will ever support selecting multiple filters natively. It might make
a useful addition, but it also might make more people over-filter their photos and that would just make me sick.

Better keep this little trick between us.
