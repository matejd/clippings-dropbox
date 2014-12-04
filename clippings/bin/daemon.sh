#!/bin/sh

BASH=/mnt/us/bash
UPLOADER=/mnt/us/dropbox_uploader.sh
CLIPPINGS_FILE="/mnt/us/documents/My Clippings.txt"
UPLOAD_DEST_FILE="My Clippings.txt"
DAEMON_STATE_FILE=daemon_ip

kill_if_running()
{
    if [ -e $DAEMON_STATE_FILE ]; then
        kill `cat $DAEMON_STATE_FILE` > /dev/null 2>&1
        rm $DAEMON_STATE_FILE
    fi
}

start_daemon()
{
    echo $$ > $DAEMON_STATE_FILE
    while true; do
        lipc-wait-event com.lab126.cmd interfaceChange
        sleep 10
        WIFI_ENABLED=$(lipc-get-prop com.lab126.cmd wirelessEnable)
        if [ $WIFI_ENABLED -eq 1 ]; then
            $BASH $UPLOADER upload "$CLIPPINGS_FILE" "$UPLOAD_DEST_FILE"
        fi
    done
}

case $1 in
    start)
        kill_if_running
        start_daemon
    ;;
    stop)
        kill_if_running
    ;;
    status)
        if [ -e $DAEMON_STATE_FILE ]; then
            if ps -p `cat $DAEMON_STATE_FILE` > /dev/null 2>&1; then
                echo "running"
            else
                rm $DAEMON_STATE_FILE
                echo "not running"
            fi
        else
            echo "not running"
        fi
    ;;
esac
