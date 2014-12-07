My Clippings.txt to Dropbox
===========================

This is a KUAL (Kindle Unified Application Launcher) extension which
syncs Kindle's My Clippings.txt file via wifi to a Dropbox account.

A daemon (bash script) runs in the background. It wakes up when wifi is available
and uses [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)
to upload the clippings text file to a connected Dropbox account.

Tested on Kindle Paperwhite 2 (firmware 5.4.3.2).

Also includes a Python script that converts My Clippings.txt to CSV format.

Setup
-----

Because Dropbox-Uploader requires bash (rather than just sh), we need to get bash on Kindle first.
There might be an easier way, but I just cross-compiled bash for ARM (the toolchain
is trivial to setup on Debian).
Steps:

1. Jailbreak your Kindle (left as an exercise for the reader), set up ssh and KUAL.
2. Cross-compile bash for ARM:
  1. Get ARM toolchain (on Debian just install arm-linux-gnueabi-gcc).
  2. Get bash source at http://www.gnu.org/software/bash/ (I used version 4.3).
  3. Unpack, then
  ```
  $cd bash-4.3/
  $CC=arm-linux-gnueabi-gcc-4.9 ./configure --prefix=/mnt/us/bash/ --host=arm-linux
  $make
  ```
  4. Copy bash executable to your Kindle (to /mnt/us/).
3. Get [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) and
   copy it to Kindle as well.
4. Set up the uploader on your Kindle by running once
   ```
   $/mnt/us/bash dropbox_uploader.sh
   ```
   and follow the steps, create a custom Dropbox App, copy key & secret. Give yourself permissions.
5. Copy the entire clippings/ folder in this git repository to /mnt/us/extensions/. This
   makes the extension automatically visible to KUAL.
6. Open KUAL and start the extension daemon! The daemon won't survive a restart, I might
   fix that sometime.
