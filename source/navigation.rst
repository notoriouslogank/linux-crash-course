##########
Navigation
##########

.. _the-grand-tour:

The Grand Tour
==============

Alright, so you've read (or vaguely skimmed) the introductory section.  Hopefully, you at least *kind of* understand some of the concepts.  If, however, you feel way out of your depth, fear not: we're going to start executing some common Linux commands.  By the end of this section, you'll have a somewhat better understanding not only of the Linux file structure, but also some number of useful commands for navigating the system (as well as other common commands).

.. note::

    Don't bother trying to memorize any (or all) of these commands.  If you use the terminal for your day-to-day interactions with the system, you *will* begin to memorize the necessary commands; simply knowing a command **exists** is often enough information to be able to meaningfully research what you specifically need to do.

.. _you-are-here:

You Are Here
============

First things first: before you can go somewhere, you need to know where you've *started* (well, not **really**, actually, but let's pretend that's true for the purposes of this section).  To discover precisely *where* in the filesystem you're currently located, we're going to use the command ``pwd``.  Open a new terminal and execute the following command:

.. code-block::

    pwd

As you'll see, the shell returns the exact path you're currently "at".  In this example, unless you've otherwise navigated to a different directory, this will likely return the absolute path to your home directory.  In my case, the output reads ``/mnt/c/Users/logan/Desktop/lcc``; most likely your output will look more along the lines of ``/home/<your_username>``.

``pwd`` is quite useful in situations where you've navigated deeply into some directory to locate a particular file location and need the entire path to refer to by some other application.

So that covers how to know where within the file system your current shell is running.  But what if you want to know exactly which files and/or directories are located at that location?

.. _roll-call:

Roll Call
=========

To get a list of the files and directories located at your current location, you'll want ``ls``.

.. code-block::

    ls

If you're in your home directory -- and you're on a freshly-installed system -- you may not get an awful lot of information back here.  However, **in general** you would expect to find, perhaps, a ``Documents`` directory in your home directory.  However, we could ``ls`` anywhere we wanted to:

.. code-block::

    ls /etc/ssh

We've now provided the ``ls`` command with an *argument*: ``/etc/ssh``.  This tells the shell to list the contents of the specified directory.  You should see a list similar (but not necessarily identical) to: ``ssh_config``, ``sshd_config``, ``known_hosts``, as well (perhaps) as a number of other files.  You may also notice -- depending again on your system configuration -- that Linux makes no distinction in the output between a ``dir`` and a ``file``; in other system configurations, however, your terminal may output directories and files in different colors.  This can all be configured in a finely-grained manner at your discretion, but it's something to at least be **aware** of, if not yet actively change.

Now let's give ourselves a workspace to play around with some files and suchlike.

.. _mkdir:

mkdir
=====

Go ahead and run the following command:

.. code-block::

    mkdir linux-crash-course

There won't be any obvious output from this command (unless it fails, which it really shouldn't).  However, it *did* do something; go ahead and run

.. code-block::

    ls

to take a look and see what happened.

In case it wasn't painfully obvious, the ``mkdir`` command *makes* a *directory* -- or what you Windows veterans would call a "folder".  Now let's move *into* that directory and take a look around.

.. _move-along:

Move Along
==========

We have a destination in mind: the newly-created ``linux-crash-course`` directory.  So let's navigate *into* that directory as if we were planning to look through its' contents (or create some files):

.. code-block::

    cd linux-crash-course
    pwd

``cd`` is the Linux command for "call directory" (although I've also heard it suggested that it's "change directory", although I believe this is erroneous).