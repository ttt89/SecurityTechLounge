#!/usr/bin/env python3

from dpkt import *
from base64 import *

def iter_payload(packets):
  for t,p in packets:
    e = ethernet.Ethernet(p)
    if e.data.p != 17:
      continue
    name = dns.DNS(e.data.data.data).qd[0].name
    yield name.split(".")[0]

payload = "".join(iter_payload(pcap.Reader(open("ctf.pcap",'rb'))))
raw = b32decode(payload)

open("ctf.png", "wb").write(raw)
