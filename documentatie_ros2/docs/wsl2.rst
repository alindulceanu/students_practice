WSL2
====

.. contents:: Table of Contents
   :depth: 2
   :local:

``WSL2`` (Windows Subsystem for Linux) is a tool that allows you to use linux commands directly on your windows machine without using a VM.

WSL comes preinstalled in every windows system, but it is not activated. 


Installation
------------

In order to activate WSL2 in your machine you just need to type this command in CMD as administrator::

    wsl --install

This command will automatically choose Ubuntu as the defaul distro, if you want another linux distro do this instead::

    wsl --install -d <Distro_Name>

If you want to see a list of Distros that are available in the microsoft store, do the following::

    wsl -l -o 

Where -l stands for ``list`` and -o for ``online``


Setting up the linux user
-------------------------

Now that you have WSL2 installed, you will be asked to enter a UNIX user and password.

.. note::
    The credidentials you use do not need to be related to your windows account.

    When typing your password nothing will display on your screen. This is called blind typing and is completely normal.

    The username must be between one and eight characters long, must start with a lowercase letter or an underscore, it can contain lowercase letters, digits, underscores and dashes and can end with a dollar sign.
    
    In RegEx: ``[a-z_][a-z0-9_-]*[$]?``

    Passwords must be at least 8 characters long, they cannot be dictionary words or the same as the username, you also have to use at least 3 of 4 character sets: uppercase, lowercase, digits, symbols.

    Do not use spaces in your password!!

Now that your WSL2 setup is ready to go, don't forget to do::

    sudo apt update && sudo apt upgrade

once in a while


