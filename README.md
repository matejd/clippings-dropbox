My Clippings.txt to Dropbox
===========================

This is a KUAL (Kindle Unified Application Launcher) extension which
syncs Kindle's My Clippings.txt file via wifi to a Dropbox account.

A daemon runs in the background. It wakes up when wifi is available
and uses [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)
to upload the clippings text file to a connected Dropbox account.

Tested on Kindle Paperwhite 2.


Setup
-----

Because Dropbox-Uploader requires bash, we need to get bash on Kindle first.
Steps:
1. Jailbreak the Kindle (left as an exercise for the reader), set up ssh and KUAL.
2. Cross-compile bash for ARM:
2.1. Get ARM toolchain (on Debian just install arm-linux-gnueabi-gcc).
2.2. Get bash source at http://www.gnu.org/software/bash/ (I used version 4.3).
2.3. Unpack, then
```
cd bash-4.3/
CC=arm-linux-gnueabi-gcc-4.9 ./configure --prefix=/mnt/us/bash/ --host=arm-linux
make
```
2.4. Copy bash executable to the Kindle (to /mnt/us/).
3. Get [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) and
copy it to Kindle as well.
4. Set up the uploader on Kindle by running once
```
/mnt/us/bash dropbox_uploader.sh
```
and follow the steps, create a custom Dropbox App, copy key & secret. Give yourself permissions.
5. Copy the entire clippings/ folder in this git repository to /mnt/us/extensions/. This
makes the extension automatically visible to KUAL.
6. Open KUAL and start the extension daemon!
