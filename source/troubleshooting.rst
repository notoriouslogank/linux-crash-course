#############################
Troubleshooting Common Issues
#############################

Let's take a look at some common issues that can occur with GPU miners.  The following issues are presented in no particular order; the *troubleshooting* steps, however, *are* presented in what I would generally consider the recommended troubleshooting flow.

.. WARNING::

    Please note that this list is provided primarily as a *starting point*; please read the *entirety* of the relevant entry and **make sure** you know what the command(s) you're about to run *actually do* before simply copy/pasting commands into the terminal.  You've been warned.

.. _no-space:

No Space On Disk
================

This issue tends to arise when HiveOS is running off a USB.  Ultimately this issue is due to the way HiveOS allocates the space on its' install media.  Because -- for whatever reason -- HiveOS doesn't actually use the *entirety* of the disk but rather creates several smaller partitions on the drive, an issue can occur where the system log files can fill the entirety of the free space on the partition.  Usually this seems to happen on rigs which have been running for some time or have otherwise generated a large number of logs -- typically, but not always, due to other system errors.

As with most Linux distributions, the system log files can be found in ``/var/log``.  The miner-specific log files -- and generally the ones we want to deal with -- are located more specifically at ``/var/log/miner/<miner_name>/*.log``.

Should you run into a "No Disk Space" error, the first move is to delete the log files.  In the terminal, run the following command:


.. code-block::

    rm /var/log/<miner_name>/*

.. note::

    This command will delete **all** miner logs; if you think you might need them for further troubleshooting (or records), perhaps simply *moving* the logs to a separate disk would be more advisable.

Per the HiveOS documentation `available here <https://hiveon.com/install/#howto-image>`_, when running HiveOS from a live USB, it's often advisable to run the ``logs-off`` command immediately following system installation.  Not only will this prevent the "Disk Full" error, but it will help prolong the life of the USB as it greatly reduces the number of read/write operations performed on the system over time.


.. _no-ip:

Unable to Obtain IP Address
===========================

**COMING SOON**

.. _system-updates:

System Updates
==============

As a general rule, don't fix what ain't broke.  That means that, provided HiveOS is operating as expected, it's often a good idea to simply leave well enough alone and avoid making needless system updates (just in case something breaks).  However, there are certainly times where a system update is both advisable and necessary.  There are several ways to accomplish this.

.. _selfupgrade:

selfupgrade
-----------

This HiveOS-provided script tends to be my first port of call in terms of updates.  To run the selfupgrade script, run the following command:

.. code-block::

    selfupgrade --force

.. note::

    The ``--force`` switch is optional, but I typically include it when I'm running a selfupgrade.  This just avoids having to confirm package changes, etc.  Just be aware that using the ``--force`` flag will, as the name suggests, *force* the upgrades regardless of potential breaking errors it may encounter.

Essentially, this command updates **only** the HiveOS packages, **not** the entirety of the underlying Ubuntu system.  This is done by design on HiveOS's part, apparently to save bandwidth.  However, there are occasions where the underlying Ubuntu repositories have become out of sync for one reason or another.  When this happens, you'll find the ``selfupgrade`` returns some errors, notably "Failed to fetch <a particular package>".  In such a situation, you need to update the underlying Ubuntu repositories *first*, after which ``selfupgrade`` should run successfully:

.. code-block::

    apt update && selfupgrade --force

.. _hive-replace:

hive-replace
------------

Whereas the previous command(s) update merely the HiveOS installation, this command will update the entire system image to the newest stable version of HiveOS **and** the graphics card drivers (more on this later):

.. code-block::

    hive-replace -s -y

While straightforward enough -- run this command and move on, HiveOS will do the rest -- it's worth noting that this (generally) takes a *while* in my experience.  Many times, it will even appear that the system has entirely locked up -- I've seen the screen go blank or simply show a stationary (ie, not blinking) cursor.  Just trust the process and let it do it's thing; check back in 5-10 minutes and you'll most likely be back up and running.

If for some reason you'd like to install some arbitary HiveOS image (not necessarily the most recent stable version), you can get a list of available images with:

.. code-block::

    hive-replace -l

.. _graphics-drivers:

Drivers Out of Date
===================

Generally, it is inadvisable to update drivers (or the HiveOS installation itself) if everything is functioning properly.  However, there *are* times when updating the GPU drivers becomes necessary.  Ultimately there are several ways this can be done, depending on your specific situation.

As previously-mentioned, ``hive-replace -l`` should be comprehensive in updating both the HiveOS system image as well as the drivers.  If you've run ``hive-replace -l``, you've updated the drivers as well (provided nothing's gone horribly awry).

However, there are occasions when you'd like to specifically (and **only**) update the graphics drivers.  You'll need to know whether you're running Nvidia graphics cards or AMD cards, then use the relevant command(s):

.. _nvidia-drivers:

Nvidia Graphics Drivers
-----------------------

For the most up-to-date Nvidia drivers, use the HiveOS provided command:

.. code-block::

    nvidia-driver-update

If, for whatever reason, you'd like to install a *particular* driver that **is not** necessarily the most recent driver for that card, you can get a list of available drivers as such:

.. code-block::

    nvidia-driver-update --list

This will return a list of available drivers and allow you to select a specific version.  Or, if you already know the exact driver you'd like to install, you can install it with:

.. code-block::

    nvidia-driver-update <xxx.xx>

Where <xxx.xx> is the exact driver version you'd like to install.

.. note::

    Occasionally, updating the drivers can cause the overclocking settings to break.  Usually you can fix this issue with ``apt install --reinstall -y nvidia-settings``.  It may be necessary to enter maintenance mode to get this command to work (as maintenance mode operates without loading the graphics drivers).

.. _amd-drivers:

AMD Graphics Drivers
--------------------

.. WARNING::

    While HiveOS **does** provide a builtin script to update AMD drivers independantly from the rest of the system, HiveOS **does not** recommend doing so.  More information is available `here <https://hiveon.com/knowledge-base/guides/driver_upd/>`_.

If you've read the above warning and would like to proceed *anyway*, you can use the HiveOS builtin AMD GPU update script:

.. code-block::

    amd-ocl-install

This will provide a list of available drivers from which to choose.

.. _no-post:

No POST
=======

**COMING SOON**

.. _boot-loop:

Boot Loop
=========

**COMING SOON**