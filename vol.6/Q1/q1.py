#!/usr/bin/env python3

from dpkt import *
from itertools import *

def b2i(bits):
  ret = 0
  for bit in bits:
    ret = (ret*2)|bit
  return ret

def isplit(it, sep):
  it = iter(it)
  run = True
  def part():
    for e in it:
      if e == sep:
        return
      yield e
    nonlocal run
    run = False
  while run:
    yield list(part())

p = pcapng.Reader(open("packet",'rb'))
lenmap = {98:None, 99:0, 153:1}

bits = [lenmap[len(b)] for t,b in islice(p, None, None, 2)]

print(bytes(b2i(x) for x in isplit(bits, None) if x))
