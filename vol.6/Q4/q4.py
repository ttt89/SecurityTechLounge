#!/usr/bin/env python3

from ctypes import *
import sys

if sys.maxsize != 2**63-1:
  print("use x64")
  exit()

libc = CDLL('libc.so.6')

enter = b'UH\x89\xe5' # push rbp; mov rbp, rsp;
sc = enter + bytes.fromhex(open('sc').read().replace('\n',''))

c_sc = c_char_p(sc)
size = len(sc)
addr = c_void_p(libc.valloc(size))
memmove(addr, c_sc, size)
libc.mprotect(addr, size, 0x7)
cast(addr, CFUNCTYPE(c_void_p))()
print()

