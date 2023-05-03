title: Data Interchange Formats
urlname: data-interchange-formats
date: 2013-01-03T21:55

Today while doing some programming work I had the opportunity to take a closerlook at CSV and JSON. My programming experience up to this point has really onlyincluded consuming these formats. Today I wrote code to produce these formats.

We have an application where I work that exports data to a MySQL database. Awhile age, I wrote [a very simple web app](https://github.com/williamjacksn/fresnel) to make viewing reports from thatdata easier. Until today, the reports were only available as tables in an HTMLpage.

After the work I did today, the same reports are now available as CSV (to easilyimport into spreadsheet apps like Excel and Numbers) and JSON (to easily passthe data to other external applications).

It was enlightening to learn about the quirks of both formats. I had neverbefore considered things like what characters need to be escaped in strings andwhat character encoding I ought to use.

It seems like whenever I get deep into programming where text input and outputis concerned, I always run into problems with character encodings. I complainabout this to my programming-minded friends often.

I honestly don&#x02bc;t know what use the JSON output will be, but I was in themood so I added it.

I hope to write about my web app in greater detail in the future.