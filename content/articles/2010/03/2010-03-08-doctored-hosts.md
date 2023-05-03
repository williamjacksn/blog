title: Blocking ads and malware with a doctored hosts file
urlname: doctored-hosts
date: 2010-03-08T11:08

__NOTE:__ When I use the method described here, Forefront Endpoint Protection 2010 repeatedly detects [SettingsModifier:Win32/PossibleHostsFileHijack](http://www.microsoft.com/security/portal/Threat/Encyclopedia/Entry.aspx?threatid=14994) on the client.

---

Replacing the default `hosts` file is a great way to block ads and malware while browsing the Internet. An oft-updated malware-blocking `hosts` file, along with instructions for how to use it, can be found on [this great Windows troubleshooting website](http://www.mvps.org/winhelp2002/hosts.htm).

Deploying the doctored `hosts` file on a single computer is elementary. Deploying the doctored `hosts` file to several hundred managed systems is much more fun and rewarding. It is also rather easy, thanks to Group Policy Preferences. Here&#x02bc;s how you do it:

In __Group Policy Management Editor__, browse down to __Computer Configuration\\Preferences\\Windows Settings\\Files__.

![Group Policy Preferences: Files](https://dl.dropboxusercontent.com/s/ta4wevnic9s8g0v/20100308-gpp-files.jpg)

Right-click on __Files__ and choose __New → File__. Set the __Action__ to __Replace__ (__Update__ does not work, because it will not overwrite a file that already exists; it will only change attributes). Set the __Source file(s)__ to `%gptpath%\\files\\hosts` and the __Destination File__ to `%systemdir%\\drivers\\etc\\hosts`. Check the __Archive Attribute__, but leave everything else unchecked.

![Group Policy Preferences: hosts](https://dl.dropboxusercontent.com/s/4t6cnaxle4mp4vm/20100308-gpp-hosts.jpg)

`%gptpath%` is a magic little variable that resolves to a folder in `SYSVOL` where all the settings for this Group Policy Object are saved. In this case, it will resolve to `...\\Policies\\{gpo-unique-id}\\Machine`. Inside that folder you should already see two more folders: `Preferences` and `Scripts`. Create a new folder called `Files` and put the hosts file you downloaded from the previously-linked website in the `Files` folder.

In truth, you can put the source file anywhere, and modify the GPO accordingly, but I put it in this particular folder so I don&#x02bc;t have to mess with NTFS permissions on the source file. If a computer can read the Group Policy Object, then it will be able to read everything in these folders in `SYSVOL`. Unless you go and explicitly change permissions on your source file. Now why would you do a thing like that?

Now save the GPO and test it out. Once you are convinced it works as advertised and doesn&#x02bc;t mess up your environment, link it wherever you want. Now sleep a little better at night.

Don&#x02bc;t forget to check the previously-linked website periodically for new versions of the `hosts` file.