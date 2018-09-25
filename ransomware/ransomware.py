# uncompyle6 version 3.2.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.0 (default, Sep 15 2018, 19:13:07)
# [GCC 8.2.1 20180831]
# Embedded file name: ransomware.py
# Compiled at: 2018-09-04 16:35:11
import string
from random import *
import itertools

def caesar_cipher(word, key):
    key = key * (len(word) / len(key) + 1)
    return ('').join((chr(ord(a) ^ ord(b)) for a, b in itertools.izip(word, key)))


f = open('./FlagDCTF.pdf', 'r')
buf = f.read()
f.close()
allchar = string.ascii_letters + string.punctuation + string.digits
password = ('').join((choice(allchar) for i in range(randint(60, 60))))
buf = caesar_cipher(buf, password)
f = open('./youfool!.exe', 'w')
buf = f.write(buf)
f.close()
# okay decompiling ransomware.pyc
