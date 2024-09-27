#####
Intro
#####

.. _what-the-fuck-is-a-linux:

What the fuck is a Linux?
=========================

.. note::

    Please don't take anything in this guide as 100% gospel.  While I've done my best to ensure I'm not giving you any outright erroneous information, it's entirely possible that I either have forgotten something vital, misunderstood something on a fundamental level, or your individual system configuration is in conflict with the information expressed in this guide.  Please do your own research if you'd like further information about anything contained in this guide; use this guide at your own risk.  I'm not responsible for you bricking your shit.


Linux is an operating system, like Windows or MacOS.  Unless you ask a huge nerd, who will happily tell you Linux is a *kernel*; Ubuntu (or Debian, or Arch btw) are *operating systems*.  Even huger nerds will probably tell me why I'm wrong, but fuck 'em.

Look, I'm not going to bore you with the details - who (Linus Torvalds), when (late 80s/early 90s), why (Linus is a bit of a contrarian; also boredom) - don't really matter for our purposes.  Feel free to investigate on your own time.

Fundamentally, these are the things you should keep in mind:

.. _everything-is-a-file:

Everything is a File
====================

So what do I mean by that?  In Linux, we conceptualize everything as a file (or folder, though we often call that a `dir` as in **directory**.) So whereas on Windows you'd often have to, say, open a program and reconfigure its' settings within the software, in Linux you'll often *edit* -- in a text editor -- the actual values of data within a file.  In Windows, you rely on the GUI to make most changes; in Linux, there are times the command line is either the only or the **best** option.

This is relevant in deeper ways, but we won't get into those right now.

.. _superusers:

The Superuser
=============

Unlike Windows, Linux is **extremely** security-concious.  This isn't to say Windows is *especially* poor in terms of security; however, default Windows configurations are **extremelly** (read: dangerously) lax with respect to file permissions -- so much so that it's possible the concept of "file permissions" is somewhat alien.

Whereas in Windows you might right click something and "Run As Administrator", in Linux you'd instead log into the so-called superuser account (although much more frequently you'll hear this administrative account referred to as "root").

Let's imagine we need to reconfigure some SSH settings on a system-wide level.  As this action is potentially extremely dangerous (in terms of potentially opening the machine up to  possible attack vectors), Linux doesn't allow just *anyone* to fuck around with such files.

I'll illustrate what I mean. First, we're going to open our SSH configuration file in a text editor (in this case we're using nano, but there are myriad text editors you could use).

.. code-block:: bash

    nano /etc/ssh/ssh_config

Depending on your distribution, level of administrative access, etc., you likely either *immediately* got an error which disallowed you to open the file *at all*.  However, most distributions with which I'm familiar will in fact let you open the file in a text editor.  If so, go ahead and add the following to the very end of the open file: ``# this is just a pointless comment to illustrate a point``.

Once you've added that (or whatever text you'd like, really), go ahead and try to write the changes to the file.  By default in nano, the hotkeys are Ctrl+X to exit; you'll receive a message asking whether or not you'd like to "save the modified buffer" -- that is, write your changes to disk.  If you say "yes", you'll quickly find yourself faced with another error: you lack the proper permissions to write to this file location.

So what, then, is to be done?  Well, you **could** login to the root account on the system, assuming you know the root password (and depending a bit on the individual system configuration):

.. code-block:: bash

    su root
    nano /etc/ssh/ssh_config

So what are we doing here?  Firstly, we're logging into an entirely different user account -- in this case ``root``, the most fundamental administrative account on any Linux system.  If you have "root access", you can execute **any** command the machine is capable of -- often without so much as a confirmation.  In the second line, we're simply doing what we've seen prior: we're opening the configuration file for editing.  You'll notice that now, however, you should be able to edit the file **and** save the changes to disk.

Once you switch to the root account, you'll also notice that your prompt changes.  Whereas before you'd see, "<username>@<hostname>:" (or similar), you'll notice the username has changed to "root@<hostname>".  Now, any command you execute will be run -- often without asking for further confirmation.

You may notice that this presents some potentially major issues, the primary of which is: when you inevitably forget to log back **out** of the root account, and you make some sort of change that was **intended** to be made locally (as your username), you instead make that change **globally**.  As such, it is often considered poor form to actually switch to the root account -- a better solution would be some way to *temporarily* login to the root account, just long enough to perform the necessary task(s), and ensuring you log back *out* of the root account before you **fuck everything up**.  Enter: ``sudo``!

Let's look at the exact same task (editing your SSH configuration file), using sudo:

.. code-block:: bash

    sudo nano /etc/ssh/ssh_config

Provided you know the requisite password, you should now be able to edit and save the configuration file *without* having to actually switch to another user account.  The magic here comes from the ``sudo`` argument we've prepended to the command.  Sudo is short for "superuser do"; in other words, we're telling the superuser (the root user) to "do" (ie, execute) a particular command (or commands).  We don't have to remember to log back out of anything, because as soon as we've run our command, we're right back to whatever our username was before.  This is considered *much* safer than logging into the root account entirely, though it should be noted that any command run with "sudo" *will be treated as if run by the root user*.  In other words, be careful.

.. WARNING::

    It is **extremely** bad practice to execute commands using 'sudo' unless you are absolutely sure what the command is going to do, and unless **absolutely necessary** for the command to execute correctly.  If you can do it *without* invoking 'sudo', there are almost *no* situations where it is preferable to do otherwise.

.. _root-directory:

/ for the Home Team
===================

One of the most important principles to understand about Linux is that the way in which drives (and therefore directories and files lower in the hierarchy) are named are fundamentally different than Windows -- if you've used MacOS, my understanding is that this will be much more familiar.

First: rather than a ``C:`` (or D, or X) drive, Linux refers to every file location relative to ``/``.

That's not a typo: the base directory for the entire filestructure is ``/``, pronounced "root".  This isn't to be confused with the concept of "root access" -- but more on that later.  Moving down the hierarchy from ``/``, let's look at a user's "home" directory.

You can think of the "home" directory as an equivalent of a Windows user's "Desktop" folder.  Essentially this is where user-specific files, settings, etc. are stored -- they're available only to the user who owns the directory (by default), and permission is denied to other users on the machine (again, by default -- this can be changed).  So where would you find your home directory? Let's take a look at an example:

Let's assume our machine has two users, "Bob" and "Frank".  Inside the root directory -- ``/`` -- you'll find a ``home`` directory.  Within **that**, you'd expect to find two directories: ``bob`` and ``frank``.

.. _oh-the-places-youll-go:

Oh, the Places You'll Go
========================

I won't delve **too** deeply into the other directories located in the root directory, but some other important directories directly off ``/`` include:

/etc
    This directory hold many configuration files for various aspects of the system.  Note that the configuration files in ``/etc`` are *system-wide*, not *user-specific*.
/bin
    This directory contains *most* of the binary files which comprise individual programs.  So if you install something from a standard Linux repository -- and install it *system-wide* -- it'll most likely install here.
/dev
    This directory lists all "block devices" on the system.  Without getting too deep into the concept of block devices, suffice to say that this directory lists all *physical or virtual* devices on the system.  So if you want to, for instance, wipe your secondary hard disk, you'd probably take a look in ``/dev`` to find the particular device.
/tmp
    This is somewhat self-explanatory: it holds files which are only extant for a limited period of time, often only during the runtime of a particular application.  However, it is sometimes useful to write files to ``/tmp`` such that they automatically delete themselves after a reboot.
/mnt
    This directory contains your *mounted* drives (or other block devices, although unless you're doing something quite esoteric, you're mostly going to be looking for drives in ``/mnt``).  So let's say you plug in a USB drive, and want to browse through the files on the drive: you're going to want to take a look within ``/mnt``.

.. note::
    This list of directories is far from comprehensive.  Depending upon your particular distribution -- as well as your specific system configuration -- the directories in the ``/`` directory may vary.  However, the aforementioned directories are pretty typical for the vast majority of distributions.

