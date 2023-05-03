title: Creating, modifying, and deleting shortcuts the easy way
urlname: gpp-shortcuts
date: 2010-05-05T08:02

A colleague recently asked me for help with a VBScript she was working with. The purpose of the script was to change the target of a shortcut that was sitting on the Desktop of a number of computers in her environment. Her intent was to set this script to run at startup or logon and edit the shortcut to point to a new target.

Things got a little more complicated when she discovered that the shortcut might be on the user&#x02bc;s personal desktop, on the All Users desktop (this was Windows XP), or even in the Default User desktop. The standard for setting this shortcut changed over time, so now her environment wasn&#x02bc;t homogeneous.

And you thought only milk could be homogeneous?

Two years ago, I would have merrily worked out a script without giving this a second thought. But today, there is a better way. You don&#x02bc;t need to pull out your hair debugging a script to take care of this. Enter Group Policy Preferences.

I am often surprised when I find someone who doesn&#x02bc;t know about Group Policy Preferences, because they have been around since Windows Vista and Server 2008. The most attractive description I can give of Group Policy Preferences is that they will make 99% of your startup/shutdown and logon/logoff scripts obsolete. But mapped drives, networked printers, and desktop shortcuts are only the beginning. You can set just about anything in the registry, too.

I say &ldquo;just about&rdquo; anything because I haven&#x02bc;t tried to set everything in the registry yet. But everything I _have_ tried has worked.

Now, enough marketing. Let&#x02bc;s get down to business: creating, modifying, and deleting shortcuts using Group Policy Preferences.

In __Group Policy Management Editor__, browse down to __Computer Configuration\\Preferences\\Windows Settings\\Shortcuts__.

![Group Policy Preferences: Shortcuts](https://dl.dropboxusercontent.com/s/ye9zchrp8mq7bhn/20100505-gpp-shortcuts.jpg)

Right-click on __Shortcuts__ and choose __New → Shortcut__. Set the __Action__ to __Replace__. __Replace__ is a good choice for __Action__ because it will create a shortcut if it doesn&#x02bc;t already exist, it will overwrite a shortcut that already exists, and it will give you the option of removing the shortcut when the computer or user falls out of the scope of the Group Policy Object.

If you are trying to overwrite an existing shortcut in your environment, then __Name__ and __Location__ need to match the name and location of the existing shortcut. In this example, we will set __Name__ to `site-licensed on Austin Disk` and set __Location__ to `All Users Desktop` using the drop-down list.

>  
> If you are dealing with shortcuts on individual users&#x02bc; desktops, you should configure the shortcut in the __User Configuration__ section and set __Location__ to `Desktop` using the drop-down list.
> 

Set __Target type__ to the type of thing the shortcut will point to. For network shares, choose `File System Object`.

Set __Target path__ to the target of the shortcut. In this example, I want the shortcut to point to a network share at `\\\\austin.utexas.edu\\disk\\site-licensed`.

>  
> If you set __Target type__ to `URL`, this field is called __Target URL__. If you set __Target type__ to `Shell Object`, this field is called __Target object__.
> 

If you want, you can choose an icon for the shortcut by clicking on the __\[&hellip;\]__ button next to __Icon file path__.

![Group Policy Preferences: Shortcuts Example](https://dl.dropboxusercontent.com/s/dxlvpxddl6wxwsa/20100505-gpp-shortcuts-example.jpg)

Save the Shortcut and link the Group Policy Object. When Group Policy updates on your clients, behold a shortcut appear (or be replaced) on the desktop!

For more details on what you can do with Shortcuts in Group Policy Preferences, click the __Help__ button while editing a Shortcut item.