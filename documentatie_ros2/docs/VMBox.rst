VMBox
================================

Welcome to Oracle VM VirtualBox.
**********************************

Oracle VM VirtualBox is a cross-platform virtualization application. What does that mean? For one thing, it installs on your existing Intel or AMD-based computers, whether they are running Windows, macOS, Linux, or Oracle Solaris operating systems (OSes). Secondly, it extends the capabilities of your existing computer so that it can run multiple OSes, inside multiple virtual machines, at the same time. As an example, you can run Windows and Linux on your Mac, run Windows Server on your Linux server, run Linux on your Windows PC, and so on, all alongside your existing applications. You can install and run as many virtual machines as you like. The only practical limits are disk space and memory.

Oracle VM VirtualBox is deceptively simple yet also very powerful. It can run everywhere from small embedded systems or desktop class machines all the way up to datacenter deployments and even Cloud environments.

Why is Virtualization Useful?
******************************

The techniques and features that Oracle VM VirtualBox provides are useful in the following scenarios:

 * Running multiple operating systems simultaneously. Oracle VM VirtualBox enables you to run more than one OS at a time. This way, you can run software written for one OS on another, such as Windows software on Linux or a Mac, without having to reboot to use it. Since you can configure what kinds of virtual hardware should be presented to each such OS, you can install an old OS such as DOS or OS/2 even if your real computer's hardware is no longer supported by that OS.

 * Easier software installations. Software vendors can use virtual machines to ship entire software configurations. For example, installing a complete mail server solution on a real machine can be a tedious task. With Oracle VM VirtualBox, such a complex setup, often called an appliance, can be packed into a virtual machine. Installing and running a mail server becomes as easy as importing such an appliance into Oracle VM VirtualBox.

 * Testing and disaster recovery. Once installed, a virtual machine and its virtual hard disks can be considered a container that can be arbitrarily frozen, woken up, copied, backed up, and transported between hosts.

 * Using virtual machines enables you to build and test a multi-node networked service, for example. Issues with networking, operating system, and software configuration can be investigated easily.

 * In addition to that, with the use of another Oracle VM VirtualBox feature called snapshots, one can save a particular state of a virtual machine and revert back to that state, if necessary. This way, one can freely experiment with a computing environment. If something goes wrong, such as problems after installing software or infecting the guest with a virus, you can easily switch back to a previous snapshot and avoid the need of frequent backups and restores.

 * Any number of snapshots can be created, allowing you to travel back and forward in virtual machine time. You can delete snapshots while a VM is running to reclaim disk space.

 * Infrastructure consolidation. Virtualization can significantly reduce hardware and electricity costs. Most of the time, computers today only use a fraction of their potential power and run with low average system loads. A lot of hardware resources as well as electricity is thereby wasted. So, instead of running many such physical computers that are only partially used, one can pack many virtual machines onto a few powerful hosts and balance the loads between them.
 
Some Terminology
*******************

When dealing with virtualization, and also for understanding the following chapters of this documentation, it helps to acquaint oneself with a bit of crucial terminology, especially the following terms:

 * Host operating system (host OS). This is the OS of the physical computer on which Oracle VM VirtualBox was installed. There are versions of Oracle VM VirtualBox for Windows, macOS, Linux, and Oracle Solaris hosts.

 * Most of the time, this manual discusses all Oracle VM VirtualBox versions together. There may be platform-specific differences which we will point out where appropriate.

 * Guest operating system (guest OS). This is the OS that is running inside the virtual machine. Theoretically, Oracle VM VirtualBox can run any x86 OS such as DOS, Windows, OS/2, FreeBSD, and OpenBSD. But to achieve near-native performance of the guest code on your machine, we had to go through a lot of optimizations that are specific to certain OSes. So while your favorite OS may run as a guest, we officially support and optimize for a select few, which include the most common OSes.

 * Virtual machine (VM). This is the special environment that Oracle VM VirtualBox creates for your guest OS while it is running. In other words, you run your guest OS in a VM. Normally, a VM is shown as a window on your computer's desktop. Depending on which of the various frontends of Oracle VM VirtualBox you use, the VM might be shown in full screen mode or remotely on another computer.

 * Internally, Oracle VM VirtualBox treats a VM as a set of parameters that specify its behavior. Some parameters describe hardware settings, such as the amount of memory and number of CPUs assigned. Other parameters describe the state information, such as whether the VM is running or saved.

 * You can view these VM settings in VirtualBox Manager, in the Settings window, and by running the VBoxManage command.

 * Guest Additions. This refers to special software packages which are shipped with Oracle VM VirtualBox but designed to be installed inside a VM to improve performance of the guest OS and to add extra features.

Features Overview
*******************

The following is a brief outline of Oracle VM VirtualBox's main features:

 * Portability. Oracle VM VirtualBox runs on a large number of 64-bit host operating systems.

Oracle VM VirtualBox is a so-called hosted hypervisor, sometimes referred to as a type 2 hypervisor. Whereas a bare-metal or type 1 hypervisor runs directly on the hardware, Oracle VM VirtualBox requires an existing OS to be installed. It can thus run alongside existing applications on that host.

To a very large degree, Oracle VM VirtualBox is functionally identical on all of the host platforms, and the same file and image formats are used. This enables you to run virtual machines created on one host on another host with a different host OS. For example, you can create a virtual machine on Windows and then run it on Linux.

In addition, virtual machines can easily be imported and exported using the Open Virtualization Format (OVF), an industry standard created for this purpose. You can even import OVFs that were created with a different virtualization software.

For users of Oracle Cloud Infrastructure the functionality extends to exporting and importing virtual machines to and from the cloud. This simplifies development of applications and deployment to the production environment.

 * Guest Additions: shared folders, seamless windows, 3D virtualization. The Oracle VM VirtualBox Guest Additions are software packages which can be installed inside of supported guest systems to improve their performance and to provide additional integration and communication with the host system. After installing the Guest Additions, a virtual machine will support automatic adjustment of video resolutions, seamless windows, accelerated 3D graphics and more.

In particular, Guest Additions provide for shared folders, which let you access files on the host system from within a guest machine.

 * Comprehensive hardware support. Among other features, Oracle VM VirtualBox supports the following:

 * Guest multiprocessing (SMP). Oracle VM VirtualBox can present up to 32 virtual CPUs to each virtual machine, irrespective of how many CPU cores are physically present on your host.

 * USB device support. Oracle VM VirtualBox implements a virtual USB controller and enables you to connect arbitrary USB devices to your virtual machines without having to install device-specific drivers on the host. USB support is not limited to certain device categories.

 * Hardware compatibility. Oracle VM VirtualBox virtualizes a vast array of virtual devices, among them many devices that are typically provided by other virtualization platforms. That includes IDE, SCSI, and SATA hard disk controllers, several virtual network cards and sound cards, virtual serial and parallel ports and an Input/Output Advanced Programmable Interrupt Controller (I/O APIC), which is found in many computer systems. This enables easy cloning of disk images from real machines and importing of third-party virtual machines into Oracle VM VirtualBox.

 * Full ACPI support. The Advanced Configuration and Power Interface (ACPI) is fully supported by Oracle VM VirtualBox. This enables easy cloning of disk images from real machines or third-party virtual machines into Oracle VM VirtualBox. With its unique ACPI power status support, Oracle VM VirtualBox can even report to ACPI-aware guest OSes the power status of the host. For mobile systems running on battery, the guest can thus enable energy saving and notify the user of the remaining power, for example in full screen modes.

 * Multiscreen resolutions. Oracle VM VirtualBox virtual machines support screen resolutions many times that of a physical screen, allowing them to be spread over a large number of screens attached to the host system.

 * Built-in iSCSI support. This unique feature enables you to connect a virtual machine directly to an iSCSI storage server without going through the host system. The VM accesses the iSCSI target directly without the extra overhead that is required for virtualizing hard disks in container files.

 * PXE Network boot. The integrated virtual network cards of Oracle VM VirtualBox fully support remote booting using the Preboot Execution Environment (PXE).

 * Multigeneration branched snapshots. Oracle VM VirtualBox can save arbitrary snapshots of the state of the virtual machine. You can go back in time and revert the virtual machine to any such snapshot and start an alternative VM configuration from there, effectively creating a whole snapshot tree. You can create and delete snapshots while the virtual machine is running.

 * VM groups. Oracle VM VirtualBox provides a groups feature that enables the user to organize and control virtual machines collectively, as well as individually. In addition to basic groups, it is also possible for any VM to be in more than one group, and for groups to be nested in a hierarchy. This means you can have groups of groups. In general, the operations that can be performed on groups are the same as those that can be applied to individual VMs: Start, Pause, Reset, Close (Save state, Send Shutdown, Poweroff), Discard Saved State, Show in File System, Sort.

 * Clean architecture and unprecedented modularity. Oracle VM VirtualBox has an extremely modular design with well-defined internal programming interfaces and a clean separation of client and server code. This makes it easy to control it from several interfaces at once. For example, you can start a VM simply by clicking on a button in the Oracle VM VirtualBox graphical user interface and then control that machine from the command line, or even remotely.

Due to its modular architecture, Oracle VM VirtualBox can also expose its full functionality and configurability through a comprehensive software development kit (SDK), which enables integration of Oracle VM VirtualBox with other software systems.

 * Remote machine display. The VirtualBox Remote Desktop Extension (VRDE) enables high-performance remote access to any running virtual machine. This extension supports the Remote Desktop Protocol (RDP) originally built into Microsoft Windows, with special additions for full client USB support.

The VRDE does not rely on the RDP server that is built into Microsoft Windows. Instead, the VRDE is plugged directly into the virtualization layer. As a result, it works with guest OSes other than Windows, even in text mode, and does not require application support in the virtual machine either. The VRDE is described in detail in Section 7.1, “Remote Display (VRDP Support)”.

On top of this special capacity, Oracle VM VirtualBox offers you more unique features:

 * Extensible RDP authentication. Oracle VM VirtualBox already supports Winlogon on Windows and PAM on Linux for RDP authentication. In addition, it includes an easy-to-use SDK which enables you to create arbitrary interfaces for other methods of authentication.

 * USB over RDP. Using RDP virtual channel support, Oracle VM VirtualBox also enables you to connect arbitrary USB devices locally to a virtual machine which is running remotely on an Oracle VM VirtualBox RDP server.

Supported Host Operating Systems
**********************************

Currently, Oracle VM VirtualBox runs on the following host OSes:

Windows hosts (64-bit):

 * Windows 8.1

 * Windows 10

 * Windows 11 21H2

 * Windows Server 2012

 * Windows Server 2012 R2

 * Windows Server 2016

 * Windows Server 2019

 * Windows Server 2022

macOS hosts (64-bit):

 * 10.15 (Catalina)

 * 11 (Big Sur)

 * 12 (Monterey)

Intel hardware is required.

An installer package is available for macOS/Arm64, for systems using an Apple silicon CPU. With this package, you can run some guest operating systems for Intel x86/x64 CPUs in an emulation.

The macOS/Arm64 installer package for Apple silicon platform is available as a Developer Preview release. This package represents a work in progress project and the performance is very modest.

.. note:: Developer Preview is a public release for developers, which provides early access to unsupported software release and features.

Linux hosts (64-bit). Includes the following:

 * Ubuntu 18.04 LTS, 20.04 LTS and 22.04

 * Debian GNU/Linux 10 ("Buster") and 11 ("Bullseye")

 * Oracle Linux 7, 8 and 9

 * CentOS/Red Hat Enterprise Linux 7, 8 and 9

 * Fedora 35 and 36

 * Gentoo Linux

 * SUSE Linux Enterprise server 12 and 15

 * openSUSE Leap 15.3

It should be possible to use Oracle VM VirtualBox on most systems based on Linux kernel 2.6, 3.x, 4.x or 5.x using either the Oracle VM VirtualBox installer or by doing a manual installation. However, the formally tested and supported Linux distributions are those for which we offer a dedicated package.

Note that Linux 2.4-based host OSes are no longer supported.

Oracle Solaris hosts (64-bit only). The following versions are supported with the restrictions listed in Chapter 14, Known Limitations:

 * Oracle Solaris 11.4

Note that any feature which is marked as experimental is not supported. Feedback and suggestions about such features are welcome.

Host CPU Requirements
**********************

SSE2 (Streaming SIMD Extensions 2) support is required for host CPUs.

Starting Oracle VM VirtualBox
*******************************

After installation, you can start Oracle VM VirtualBox as follows:

 * Windows hosts. In the Programs menu, click on the item in the VirtualBox group. On some Windows platforms, you can also enter VirtualBox in the search box of the Start menu.

 * macOS hosts. In the Finder, double-click on the VirtualBox item in the Applications folder. You may want to drag this item onto your Dock.

 * Linux or Oracle Solaris hosts. Depending on your desktop environment, an Oracle VM VirtualBox item may have been placed in either the System or System Tools group of your Applications menu. Alternatively, you can enter VirtualBox in a terminal window.

When you start Oracle VM VirtualBox, the VirtualBox Manager interface is shown.

VirtualBox Manager
********************

VirtualBox Manager is the user interface for Oracle VM VirtualBox. You can use VirtualBox Manager to create, configure, and manage your virtual machines.

This section describes the main features of the VirtualBox Manager user interface. Subsequent sections and chapters describe how to use VirtualBox Manager to perform tasks in Oracle VM VirtualBox.

When you start Oracle VM VirtualBox, the VirtualBox Manager window is displayed.

The main components of the VirtualBox Manager window are as follows:

 * The machine list. The left pane of the VirtualBox Manager window lists all your virtual machines. If you have not yet created any virtual machines, this list is empty.

 * The Details pane. The pane on the right displays the properties of the currently selected virtual machine. If you do not have any machines yet, the pane displays a welcome message.

The toolbar buttons on the Details pane can be used to create and work with virtual machines.

 * Help Viewer. A window that displays context-sensitive help topics for VirtualBox Manager tasks.

The Machine List
*********************

The list of virtual machines in the left pane is called the machine list.

The following methods can be used to control and configure virtual machines in the machine list:

 * Right-click on the virtual machine name, to display menu options.

 * Click on the Machine Tools menu, to the right of the virtual machine name.

 * Click a button in the toolbar in the Details pane.

The Details Pane
******************

The Details pane shows configuration information for a virtual machine that is selected in the machine list. The pane also includes a toolbar for performing tasks.

The Details pane includes the following:

VirtualBox Manager Toolbar
***************************

A toolbar at the top of the Details pane contains buttons that enable you to configure the selected virtual machine, or to create a new virtual machine.

The toolbar includes the following buttons:

 * New. Creates a new virtual machine, and adds it to the machine list.

 * Add. Adds an existing virtual machine to the machine list.

 * Settings. Displays the Settings window for the virtual machine, enabling you to make configuration changes.

 * Discard. For a running virtual machine, discards the saved state for the virtual machine and closes it down.

 * Show/Start. For a running virtual machine, Show displays the virtual machine window. For a stopped virtual machine, Start displays options for powering up the virtual machine.

Settings
**********

A summary of settings is shown for the virtual machine.

You can change some virtual machine settings, by clicking on the setting in the Details pane.

.. note:: If a virtual machine is running, some settings cannot be altered. You must stop the virtual machine first in order to change the setting.

Virtual machine settings can also be changed using the Settings button on the VirtualBox Manager toolbar.

The virtual machine settings on the Details pane are organized in sections that correspond to those used in the Settings window.

Click the arrow icon to hide or show each section.

Preview Window
***************

The virtual machine display is shown in a small window.

You can use the Preview window to check if your virtual machine has finished booting up.

Click the arrow icon to hide or show the Preview window.

Notification Center
********************

Notification messages may be shown in a sliding panel on the right of the Details pane, called the Notification Center. Click the warning triangle to show the notification messages.

Most system messages that do not require user interaction are displayed in the Notification Center, including task failure alerts.

The progress of some tasks can be observed and stopped using the Notification Center.

VirtualBox Manager Tools
***************************

VirtualBox Manager provides two types of user tools, to enable you to perform common tasks easily.

 * Global Tools. These tools apply to all virtual machines.

 * Machine Tools. These tools apply to a specific virtual machine.

Global Tools
*************

In the left pane of the VirtualBox Manager window, click the Menu icon in the Tools banner located above the machine list. The Global Tools menu is displayed.

A drop-down list enables you to select from the following global tools:

 * Welcome. Displays the VirtualBox Manager welcome message. The VirtualBox Manager toolbar is also included, to enable you to get started with using Oracle VM VirtualBox.

 * Extensions. Displays the Extension Pack Manager tool. This tool is used to install and uninstall Oracle VM VirtualBox Extension Packs.

 * Media. Displays the Virtual Media Manager tool. This tool is used to manage the disk images used by Oracle VM VirtualBox.

 * Network. Displays the Network Manager tool. This tool is used to create and configure some types of networks used by Oracle VM VirtualBox.

 * Cloud. Displays the Cloud Profile Editor tool. This tool is used to configure connections to a cloud service, such as Oracle Cloud Infrastructure.

 * Activities. Displays the VM Activity Overview tool. This tool is used to monitor performance and resource usage of virtual machines.

The Pin icon is used to keep the Tools banner visible as you scroll down the entries in the machine list.

Machine Tools
**************

In the machine list in the left pane of the VirtualBox Manager window, select a virtual machine.

Click the Menu icon to the right of the virtual machine name. The Machine Tools menu is displayed.

A drop-down list enables you to select from the following machine tools:

 * Details. Displays the Details pane for the selected virtual machine.

 * Snapshots. Displays the Snapshots tool. This tool enables you to view and manage snapshots for the virtual machine.
 
 * Logs. Displays the Log Viewer tool. This tool enables you to view and search system logs for the virtual machine.

 * Activity. Displays the VM Activity page of the Session Information dialog. This dialog enables you to view and analyze performance metrics for the virtual machine.

 * File Manager. Displays the Guest Control File Manager tool. This tool enables you to manage files on the guest system.

Help Viewer
************

The Help Viewer is a window that displays context-sensitive help to assist you in completing common VirtualBox Manager tasks. You can display the Help Viewer in the following ways:

 * In a VirtualBox Manager wizard or dialog, click Help to display the relevant help topic.

 * In VirtualBox Manager or from a guest VM, do either of the following:

	 * Select the Help, Contents menu option.

	 * Press the F1 button.

	The keyboard shortcut used to access the Help Viewer can be configured in the Preferences window.

The Help Viewer has the following features:

 * Navigation tools. The left hand pane contains the following navigation tools:

	 * Contents. Displays the help topic location in the Oracle VM VirtualBox documentation.

	 * Search. Enables you to search the documentation for help topics.
	 
	 * Bookmarks. Enables you to bookmark useful help topics.

 * Tabbed browsing. Help topics that you have visited are displayed in tabs in the main window pane.

 * Zoomable topics. Zoom controls enable you to enlarge help topic details.

 * Printing. Help topics can be printed to PDF file or to a local printer.

About VirtualBox Manager Wizards
**********************************

VirtualBox Manager includes wizards that enable you to complete tasks easily. Examples of such tasks are when you create a new virtual machine or use the cloud integration features of Oracle VM VirtualBox.

To display a help topic for the wizard, click the Help button.

Some wizards can be displayed in either of the following modes:

 * Guided mode. This is the default display mode. Wizards are shown in the conventional manner, using a series of pages with descriptions to guide the user through the steps for a task.

 * Expert mode. This display mode is designed for more advanced users of Oracle VM VirtualBox. All settings are displayed on a single page, enabling quicker completion of tasks.

Click the button at the bottom of the wizard window to switch between Guided mode and Expert mode.

Creating Your First Virtual Machine
************************************

Click New in the VirtualBox Manager window. The Create Virtual Machine wizard is shown, to guide you through the required steps for setting up a new virtual machine (VM).

The Create Virtual Machine wizard pages are described in the following sections.

Create Virtual Machine Wizard: Name and Operating System
****************************************************************

Use this page to specify a name and operating system (OS) for the virtual machine and to change the storage location used for VMs.

You can also choose to disable the unattended guest operating system install feature.

The following fields are available on this wizard page:

 * Name. A name for the new VM. The name you enter is shown in the machine list of VirtualBox Manager and is also used for the virtual machine's files on disk.

	Be sure to assign each VM an informative name that describes the OS and software running on the VM. For example, a name such as Windows 10 with Visio.

 * Folder. The location where VMs are stored on your computer, called the machine folder. The default folder location is shown.

	Ensure that the folder location has enough free space, especially if you intend to use the snapshots feature.

 * ISO Image. Select an ISO image file. The image file can be used to install an OS on the new virtual machine or it can be attached to a DVD drive on the new virtual machine.

 * Type and Version. These fields are used to select the OS that you want to install on the new virtual machine.

	The supported OSes are grouped into types. If you want to install something very unusual that is not listed, select the Other type. Depending on your selection, Oracle VM VirtualBox will enable or disable certain VM settings that your guest OS may require. This is particularly important for 64-bit guests.

	If an ISO image is selected and Oracle VM VirtualBox detects the operating system for the ISO, the Type and Version fields are populated automatically and are disabled.

 * Skip Unattended Installation. Disables unattended guest OS installation, even if an ISO image is selected that supports unattended installation. In that case, the selected ISO image is mounted automatically on the DVD drive of the new virtual machine and user interaction is required to complete the OS installation.

	The unattended installation step in the wizard is skipped.

.. note:: This option is disabled if you do not select an installation medium in the ISO Image field.

Click Next to go to the next wizard page.

Create Virtual Machine Wizard: Hardware
****************************************

Use this page to configure hardware settings for the virtual machine.

The following fields are available on this wizard page:

 * Base Memory. Select the amount of RAM that Oracle VM VirtualBox should allocate every time the virtual machine is started. The amount of memory selected here will be taken away from your host machine and presented to the guest OS, which will report this size as the virtual machines installed RAM.

``Caution!``
Choose this setting carefully. The memory you give to the VM will not be available to your host OS while the VM is running, so do not specify more than you can spare.

For example, if your host machine has 4 GB of RAM and you enter 2048 MB as the amount of RAM for a particular virtual machine, you will only have 2 GB left for all the other software on your host while the VM is running. If you run two VMs at the same time, even more memory will be allocated for the second VM, which may not even be able to start if that memory is not available.

On the other hand, you should specify as much as your guest OS and your applications will require to run properly. A guest OS may require at least 1 or 2 GB of memory to install and boot up. For best performance, more memory than that may be required.

Always ensure that the host OS has enough RAM remaining. If insufficient RAM remains, the system might excessively swap memory to the hard disk, which effectively brings the host system to a standstill.

As with other Create Virtual Machine wizard settings, you can change this setting later, after you have created the VM.

 * Processor(s). Select the number of virtual processors to assign to the VM.

	It is not advised to assign more than half of the total processor threads from the host machine.

 * Enable EFI. Enables Extensible Firware Interface (EFI) booting for the guest OS.

Click Next to go to the next wizard page.

Create Virtual Machine Wizard: Virtual Hard Disk
**************************************************

Use this page to specify a virtual hard disk for the virtual machine.

There are many ways in which Oracle VM VirtualBox can provide hard disk space to a VM. The most common way is to use a large image file on your physical hard disk, whose contents Oracle VM VirtualBox presents to your VM as if it were a complete hard disk. This file then represents an entire hard disk, so you can even copy it to another host and use it with another Oracle VM VirtualBox installation.

The following fields are available on this wizard page:

 * Create a Virtual Hard Disk Now. Creates a new empty virtual hard disk image, located in the VM's machine folder.

	Enter the following settings:

		 * Disk Size. Use the slider to select a maximum size for the hard disk in the new VM.

		 * Pre-Allocate Full Size. This setting determines the type of image file used for the disk image. Select this setting to use a fixed-size file for the disk image. Deselect this setting to use a dynamically allocated file for the disk image.

		The different types of image file behave as follows:

			 * Dynamically allocated file. This type of image file only grows in size when the guest actually stores data on its virtual hard disk. Therefore, this file is small initially. As the drive is filled with data, the file grows to the specified size.

			 * Fixed-size file. This type of image file immediately occupies the file specified, even if only a fraction of that virtual hard disk space is actually in use. While occupying much more space, a fixed-size file incurs less overhead and is therefore slightly faster than a dynamically allocated file.

 * Use an Existing Hard Disk File. Enables you to select an existing disk image file to use with the new VM.

	The drop-down list presented in the window lists all disk images which are known by Oracle VM VirtualBox. These disk images are currently attached to a virtual machine, or have been attached to a virtual machine.

	Alternatively, click on the small folder icon next to the drop-down list. In the Hard Disk Selector window that is displayed, click Add to select a disk image file on your host disk.

 * Do Not Add a Virtual Hard Disk. The new VM is created without a hard disk.

	To prevent your physical hard disk on the host OS from filling up, Oracle VM VirtualBox limits the size of the image file. But the image file must be large enough to hold the contents of the guest OS and the applications you want to install. For a Windows or Linux guest, you will probably need several gigabytes for any serious use. The limit of the image file size can be changed later.

.. note:: You can skip attaching a virtual hard disk file to the new virtual machine you are creating. But you will then need to attach an hard disk later on, in order to install a guest operating system.

After having selected or created your image file, click Next to go to the next wizard page.

Create Virtual Machine Wizard: Summary
****************************************

This page displays a summary of the configuration for the virtual machine.

If you are not happy with any of the settings, use the Back button to return to the corresponding page and modify the setting.

Click Finish to create your new virtual machine. The virtual machine is displayed in the machine list on the left side of the VirtualBox Manager window, with the name that you entered on the first page of the wizard.

Some Examples of Unattended Installation
*****************************************

To configure unattended installation, you typically just need to specify an ISO image in the Create Virtual Machine wizard. Oracle VM VirtualBox then detects the OS type and the unattended installation process is done automatically when the wizard is completed. However, in some situations the installation may need be completed manually.

The following list describes some common scenarios for unattended installation:

 * OS type is detected automatically. The following outcomes are possible:

	 * If unattended installation is supported for the selected ISO, the guest OS is installed automatically. No user input is required.

	 * If unattended installation is not supported for the selected ISO, the ISO image is inserted automatically into the DVD drive of the new VM. The guest OS installation must then be completed manually.

 * OS type is not detected automatically. You must configure Type and Version settings in the wizard.

The ISO image is inserted automatically into the DVD drive of the new VM. The guest OS installation must then be completed manually.

 * Unattended Installation is disabled. Users can disable unattended installation, by selecting the Skip Unattended Installation check box on the initial wizard page.

The ISO image is inserted automatically into the DVD drive of the new VM. The guest OS installation must then be completed manually.

Running Your Virtual Machine
*********************************

To start a virtual machine, you have the following options:

 * Double-click on the VM's entry in the machine list in VirtualBox Manager.

 * Select the VM's entry in the machine list in VirtualBox Manager, and click Start in the toolbar the top of the window.

 * Go to the ``VirtualBox VMs`` folder in your system user's home directory. Find the subdirectory of the machine you want to start and double-click on the machine settings file. This file has a .vbox file extension.

Starting a virtual machine displays a new window, and the virtual machine which you selected will boot up. Everything which would normally be seen on the virtual system's monitor is shown in the window.

In general, you can use the virtual machine as you would use a real computer. The following topics describe a few points to note when running a VM.

Starting a New VM for the First Time
***************************************

When you start a VM for the first time the OS installation process is started automatically, using the ISO image file specified in the Create Virtual Machine wizard.

Follow the onscreen instructions to install your OS.

Capturing and Releasing Keyboard and Mouse
********************************************

Oracle VM VirtualBox provides a virtual USB tablet device to new virtual machines through which mouse events are communicated to the guest OS. If you are running a modern guest OS that can handle such devices, mouse support may work out of the box without the mouse being captured as described below.

Otherwise, if the virtual machine detects only standard PS/2 mouse and keyboard devices, since the OS in the virtual machine does not know that it is not running on a real computer, it expects to have exclusive control over your keyboard and mouse. But unless you are running the VM in full screen mode, your VM needs to share keyboard and mouse with other applications and possibly other VMs on your host.

After installing a guest OS and before you install the Guest Additions, described in Chapter 4, Guest Additions, either your VM or the rest of your computer can own the keyboard and the mouse. Both cannot own the keyboard and mouse at the same time. You will see a second mouse pointer which is always confined to the limits of the VM window. You activate the VM by clicking inside it.

To return ownership of keyboard and mouse to your host OS, Oracle VM VirtualBox reserves a special key on your keyboard: the Host key. By default, this is the right Ctrl key on your keyboard. On a Mac host, the default Host key is the left Command key. You can change this default using the Preferences window. The current setting for the Host key is always displayed at the bottom right of your VM window.

This means the following:

 * Your keyboard is owned by the VM if the VM window on your host desktop has the keyboard focus. If you have many windows open in your guest OS, the window that has the focus in your VM is used. This means that if you want to enter text within your VM, click on the title bar of your VM window first.

To release keyboard ownership, press the Host key. As explained above, this is typically the right Ctrl key.

Note that while the VM owns the keyboard, some key sequences, such as Alt+Tab, will no longer be seen by the host, but will go to the guest instead. After you press the Host key to reenable the host keyboard, all key presses will go through the host again, so that sequences such as Alt+Tab will no longer reach the guest. For technical reasons it may not be possible for the VM to get all keyboard input even when it does own the keyboard. Examples of this are the Ctrl+Alt+Del sequence on Windows hosts or single keys grabbed by other applications on X11 hosts such as the GNOME desktop Locate Pointer feature.

 * Your mouse is owned by the VM only after you have clicked in the VM window. The host mouse pointer will disappear, and your mouse will drive the guest's pointer instead of your normal mouse pointer.

Note that mouse ownership is independent of that of the keyboard. Even after you have clicked on a titlebar to be able to enter text into the VM window, your mouse is not necessarily owned by the VM yet.

To release ownership of your mouse by the VM, press the Host key.

As this behavior is inconvenient, Oracle VM VirtualBox provides a set of tools and device drivers for guest systems called the Oracle VM VirtualBox Guest Additions. These tools make VM keyboard and mouse operations much more seamless. Most importantly, the Guest Additions suppress the second "guest" mouse pointer and make your host mouse pointer work directly in the guest.

Typing Special Characters
**************************

Some OSes expect certain key combinations to initiate certain procedures. The key combinations that you type into a VM might target the host OS, the Oracle VM VirtualBox software, or the guest OS. The recipient of these keypresses depends on a number of factors, including the key combination itself.

 * Host OSes reserve certain key combinations for themselves. For example, you cannot use the Ctrl+Alt+Delete combination to reboot the guest OS in your VM, because this key combination is reserved by the host OS. Even though both Windows and Linux OSes can intercept this key combination, the host OS is rebooted automatically.

	On Linux and Oracle Solaris hosts, which use the X Window System, the key combination Ctrl+Alt+Backspace normally resets the X server and restarts the entire graphical user interface. As the X server intercepts this combination, pressing it will usually restart your host graphical user interface and kill all running programs, including Oracle VM VirtualBox, in the process.

	On Linux hosts supporting virtual terminals, the key combination Ctrl+Alt+Fx, where Fx is one of the function keys from F1 to F12, normally enables you to switch between virtual terminals. As with Ctrl+Alt+Delete, these combinations are intercepted by the host OS and therefore always switch terminals on the host.

	If, instead, you want to send these key combinations to the guest OS in the virtual machine, you will need to use one of the following methods:

	 * Use the items in the Input, Keyboard menu of the virtual machine window. This menu includes the settings Insert Ctrl+Alt+Delete and Insert Ctrl+Alt+Backspace. However, the latter setting affects only Linux guests or Oracle Solaris guests.

		This menu also includes an option for inserting the Host key combination.

	 * Use special key combinations with the Host key, which is normally the right Control key. Oracle VM VirtualBox then translates the following key combinations for the VM:

		 * Host key + Del sends Ctrl+Alt+Del to reboot the guest OS.

		 * Host key + Backspace sends Ctrl+Alt+Backspace to restart the graphical user interface of a Linux or Oracle Solaris guest.

		 * Host key + Function key. For example, use this key combination to simulate Ctrl+Alt+Fx to switch between virtual terminals in a Linux guest.

 * For some other keyboard combinations such as Alt+Tab to switch between open windows, Oracle VM VirtualBox enables you to configure whether these combinations will affect the host or the guest, if a virtual machine currently has the focus. This is a global setting for all virtual machines and can be found under File, Preferences, Input.

 * A soft keyboard can be used to input key combinations in the guest.

Changing Removable Media
*************************

While a virtual machine is running, you can change removable media in the Devices menu of the VM's window. Here you can select in detail what Oracle VM VirtualBox presents to your VM as a CD, DVD, or floppy drive.

The settings are the same as those available for the VM in the Settings window of VirtualBox Manager. But as the Settings window is disabled while the VM is in the Running or Saved state, the Devices menu saves you from having to shut down and restart the VM every time you want to change media.

Using the Devices menu, you can attach the host drive to the guest or select a floppy or DVD image.

The Devices menu also includes an option for creating a virtual ISO (VISO) from selected files on the host.

Resizing the Machine's Window
*******************************

You can resize the VM's window while that VM is running. When you do, the window is scaled as follows:

 * If you have scaled mode enabled, then the virtual machine's screen will be scaled to the size of the window. This can be useful if you have many machines running and want to have a look at one of them while it is running in the background. Alternatively, it might be useful to enlarge a window if the VM's output screen is very small, for example because you are running an old OS in it.

	To enable scaled mode, press Host key + C, or select Scaled Mode from the View menu in the VM window. To leave scaled mode, press Host key + C again.

	The aspect ratio of the guest screen is preserved when resizing the window. To ignore the aspect ratio, press Shift during the resize operation.

 * If you have the Guest Additions installed and they support automatic resizing, the Guest Additions will automatically adjust the screen resolution of the guest OS. For example, if you are running a Windows guest with a resolution of 1024x768 pixels and you then resize the VM window to make it 100 pixels wider, the Guest Additions will change the Windows display resolution to 1124x768.

 * Otherwise, if the window is bigger than the VM's screen, the screen will be centered. If it is smaller, then scroll bars will be added to the machine window.

Saving the State of the Machine
********************************

When you click on the Close button of your virtual machine window, at the top right of the window, just like you would close any other window on your system, Oracle VM VirtualBox asks you whether you want to save or power off the VM. As a shortcut, you can also press Host key + Q.

The difference between the three options is crucial. They mean the following:

 * Save the machine state: With this option, Oracle VM VirtualBox freezes the virtual machine by completely saving its state to your local disk.

	When you start the VM again later, you will find that the VM continues exactly where it was left off. All your programs will still be open, and your computer resumes operation. Saving the state of a virtual machine is thus in some ways similar to suspending a laptop computer by closing its lid.

 * Send the shutdown signal. This will send an ACPI shutdown signal to the virtual machine, which has the same effect as if you had pressed the power button on a real computer. This should trigger a proper shutdown mechanism from within the VM.

 * Power off the machine: With this option, Oracle VM VirtualBox also stops running the virtual machine, but without saving its state.

.. note:: WARNING! This is equivalent to pulling the power plug on a real computer without shutting it down properly. If you start the machine again after powering it off, your OS will have to reboot completely and may begin a lengthy check of its virtual system disks. As a result, this should not normally be done, since it can potentially cause data loss or an inconsistent state of the guest system on disk.

	As an exception, if your virtual machine has any snapshots, you can use this option to quickly restore the current snapshot of the virtual machine. In that case, powering off the machine will discard the current state and any changes made since the previous snapshot was taken will be lost.

The Discard button in the VirtualBox Manager window discards a virtual machine's saved state. This has the same effect as powering it off, and the same warnings apply.
