#!/bin/sh

if [ -e daemon_running ]; then
    return
fi

echo $$ > daemon_running

while true; do
    lipc-wait-event com.lab126.cmd interfaceChange;
    sleep 10;
    WIFI_ENABLED=$(lipc-get-prop com.lab126.cmd wirelessEnable)
    if [ $WIFI_ENABLED -eq 1 ]; then
        /mnt/us/bash /mnt/us/dropbox_uploader.sh upload /mnt/us/documents/My\ Clippings.txt My\ Clippings.txt;
    fi
done
