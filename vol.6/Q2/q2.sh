#!/bin/sh

if [ `getconf LONG_BIT` -ne "64" ]
then
 echo "use x64"
 exit
fi

chmod 755 ./ctf
tcpdump -i lo -w ctf.pcap &
sleep 2
./ctf
sleep 2
kill $!

env python3 q2.py

eog ctf.png &
