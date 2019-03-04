# README

## What is this

This is a small toy project that serves as a demonstration on how to read keyboard-data other than from the 'system keyboard' from Python.

A lot of USB-gadgets on the market today present themselves as USB-keyboards; allowing easy interfacing to any kind of application that can handle keyboard-input.

* Barcode-Scanners
* RFID-readers
* 'Gimmick' buttons
* Certain 'game-pads'
* etc.

Of course, you can simply have all input go to the shell that runs the python-script, but it would make sense to be able to 'open' the specific device and have it's output be handled by the application.

[This stackexchange post talks about handling event-data](https://unix.stackexchange.com/questions/72483/how-to-distinguish-input-from-different-keyboards)

It directly highlights one of the challenges you will face with reading raw event-data: you get key-codes, not 'letters' or 'symbols', as they are dependant on the state of other keys on the keyboard (caps-lock, shift, num-lock, etc.).. not to mention any use of the Compose-key

This script does not cover handling modifier-keys; but simply produces an upper-case+numbers representation of a string being entered and knows how to handle the "<return>" key to trigger running a handler-routine.


[Another stackexchange post](https://stackoverflow.com/questions/19732978/how-can-i-get-a-string-from-hid-device-in-python-with-evdev) has tackled part of this work already, except it's for python2 and lacks handling of <enter> key.

Hence this little toy repo


## How to use
Note that you either have to run this script as root (not encouraged) or ensure that the user it runs under has access to the correct /dev/input/event\* file
See below for more info on setting up the event-file so it can be read by generic users.


First create a directory and set up a python3 virtual env
```$ mkdir hid-reader
$ cd hid-reader
$python3 -m venv venv```


Then, activate the environment and install the required python modules using pip
```$. venv/bin/activate
$pip3 install -r requirements.txt
```

Ensure it opens the correct event-file. Have a look in /dev/input/by-path and/or /dev/inpput
For example, as root:

```
root@machine:/# ls -al /dev/input/by-path
total 0
drwxr-xr-x 2 root root 180 Mar  4 12:29 .
drwxr-xr-x 4 root root 440 Mar  4 12:29 ..
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1a.0-usb-0:1.3:1.0-event-mouse -> ../event2
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1a.0-usb-0:1.3:1.0-mouse -> ../mouse0
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1a.0-usb-0:1.4:1.0-event-mouse -> ../event3
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1a.0-usb-0:1.4:1.0-mouse -> ../mouse1
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1d.0-usb-0:1.2.4:1.0-event-kbd -> ../event5
lrwxrwxrwx 1 root root  10 Mar  4 12:29 pci-0000:00:1d.0-usb-0:1.5.1:1.0-event-kbd -> ../event14
lrwxrwxrwx 1 root root   9 Mar  4 10:38 pci-0000:00:1d.0-usb-0:1.6:1.0-event-kbd -> ../event4

root@machine:/ ls -al /dev/input/by-id
total 0
drwxr-xr-x 2 root root 180 Mar  4 14:12 .
drwxr-xr-x 4 root root 440 Mar  4 14:12 ..
lrwxrwxrwx 1 root root  10 Mar  4 14:12 usb-13ba_0001-event-kbd -> ../event14
lrwxrwxrwx 1 root root   9 Mar  4 14:08 usb-Dell_Dell_Smart_Card_Reader_Keyboard-event-kbd -> ../event4
lrwxrwxrwx 1 root root   9 Mar  4 14:07 usb-Logitech_USB_Optical_Mouse-event-mouse -> ../event3
lrwxrwxrwx 1 root root   9 Mar  4 14:07 usb-Logitech_USB_Optical_Mouse-mouse -> ../mouse1
lrwxrwxrwx 1 root root   9 Mar  4 10:38 usb-Microsoft_Microsoft_5-Button_Mouse_with_IntelliEye_TM_-event-mouse -> ../event2
lrwxrwxrwx 1 root root   9 Mar  4 10:38 usb-Microsoft_Microsoft_5-Button_Mouse_with_IntelliEye_TM_-mouse -> ../mouse0
lrwxrwxrwx 1 root root   9 Mar  4 14:08 usb-Yubico_Yubico_Yubikey_II_0001095663-event-kbd -> ../event5

```

In this case, three keyboards have been detected. A main keyboard (event4) , a YubiKey OTP-token (event5)  and a USB-gadget from the corner-shop (event14): a large foam 'ENTER' key that does what it says and nothing more.

Edit the 'hid-test.py' file and find the line at the top that opens the device.

If you set up the access-rights to the event-file correctly (or are root), you should be able to run the program and have it output parsed data to stdout; each time you press ENTER
```
$ python3 hid-test.py
... *TODO* example output here

```


*TODO* Write about:
* How to set permissions
* How to decouple a device from the kernel/shell's input-handler

