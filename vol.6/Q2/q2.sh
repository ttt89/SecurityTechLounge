#!/bin/sh

chmod 755 ./ctf
tcpdump -i lo -w ctf.pcap &
sleep 1
./ctf
kill $!
./q2.py
