#!/usr/bin/env python3

from dpkt import *
from itertools import *

def b2i(bits):
  ret = 0
  for bit in bits:
    ret = (ret*2)|bit
  return ret

def isplit(it, sep):
  l = []
  for e in it:
    if e == sep:
      yield l
      l = []
    else:
      l.append(e)
  yield l

p = pcapng.Reader(open("packet",'rb'))
d = {98:None, 99:0, 153:1}

lenmap = [d[len(b)] for t,b in islice(p, None, None, 2)]

print(bytes(b2i(x) for x in isplit(lenmap, None) if x))
