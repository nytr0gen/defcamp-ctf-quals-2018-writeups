import string
from random import *
import itertools
import os

allchar = string.ascii_letters + string.punctuation + string.digits

def hamming_dist(x, y):
    dist = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dist += 1
    return dist

def caesar_cipher(word, key):
    key = key * (len(word) // len(key) + 1)
    return ('').join((
        chr(ord(a) ^ ord(b))
        for a, b in itertools.izip(word, key)
    ))

def cacaesar_cipher(word, key, used):
    buf2 = ''
    for i in range(len(buf)):
        c = (
            chr(ord(buf[i]) ^ ord(key[i % 60]))
            if used[i % 60] else '.'
        )
        buf2 += c

    return buf2

# def decode(buf, matching):
#     key = caesar_cipher(buf[0:60], matching[0:60])
#     return caesar_cipher(buf, key)


with open('./youfool!.exe', 'rb') as f:
    buf = f.read()

# print((len(buf) - 7) % 60)

dirs = os.listdir('./examples')

# This would print all the files and directories
for file in dirs[0:1]:
    # print(file)
    with open('./examples/' + file, 'rb') as f:
        matching = f.read()

    # print(matching[0:10])


    # lastpos = (len(buf) - len(lastword)) % 60
    # matching = list(matching)
    # matching[lastpos:lastpos+len(lastword)] = lastword
    # matching = ''.join(matching)

    used = [False for _ in range(60)]
    used[0:8] = [True for _ in range(8)]
    # used[lastpos:lastpos+len(lastword)] = [True for _ in range(len(lastword))]

    # print(matching:)

    key = cacaesar_cipher(buf[0:60], matching[0:60], used)
    key = list(key[0:60])

    # lastword = '\x0a\x25\x25\x45\x4f\x46\x0a'
    # print(lastpos)
    # continue

    k = cacaesar_cipher(buf, key, used)
    # k = caesar_cipher(buf, key)

    lastword = matching[-7:]
    lastpos = len(buf) - len(lastword)
    print(lastword)
    print(len(lastword))
    print(k[lastpos:])
    lastkplm = caesar_cipher(buf[lastpos:], lastword)
    key[lastpos%60:lastpos%60+7] = lastkplm
    used[lastpos%60:lastpos%60+7] = [1] * 7

    kplm = caesar_cipher(buf[299:300], ['P'])
    key[59] = kplm[0]
    used[59] = True

    kplm = caesar_cipher(buf[958:959], ['P'])
    key[58] = kplm[0]
    used[58] = True

    kplm = caesar_cipher(buf[893:898], 'Resou')
    key[53:58] = kplm
    used[53:58] = [True for _ in range(5)]

    kplm = caesar_cipher(buf[706:712], '/Flate')
    key[46:52] = kplm
    used[46:52] = [True for _ in range(6)]

    # key = ''':P-@uSL"Y1K$[X)fg[|".45Yq9i>eV)<0C:('q4nP[hGd/E............2'''
    key = list(key)
    used = [k != '.' for k in key]

    k = cacaesar_cipher(buf, key, used)
    # print(k[-7:], matching[-7:])
    assert(k[0:8] == matching[0:8])
    assert(k[-7:] == matching[-7:])
    assert(k[299] == 'P')

    word_list = ['BitsPerComponent', '/Index', '/Page', 'Column', 'FontDescriptor', 'softwareAgent', 'Interpolate', '/FlateDecode', 'instanceID', 'ColorSpace', 'parseType', 'Resource', 'Resources', 'endstream', 'MediaBox', 'Contents', 'changed', 'Subtype', 'ProcSet', 'XObject', 'stream', 'Predictor', 'Length', 'endobj', 'action', 'Filter', 'Border', 'Parent', 'Height', 'Width', 'Image', 'Adobe', 'stEvt', 'Annot', 'Named']
    has_changed = True
    while has_changed:
        has_changed = False
        for i in range(len(k)):
            pos = 0
            best_dist = int(1e3)
            best_word = ''
            for word in word_list:
                if i + len(word) > len(k):
                    continue

                m = k[i:i+len(word)]

                # if (word == 'ProcSet' and m == '.rocSet'):
                #     print(i)
                #     'Resources'
          # '.....rces'
                if (word == '/FlateDecode' and m == '/.....Decode'):
                    print(i)
                    print('========')
                # if ((word == 'Column' and m == 'Coluqx')
                #     or (word == 'Predictor' and m == '.redictor')):
                #     best_dist = 1
                #     best_word = word
                #     best_m = m
                #     print(1337, word, m)
                #     break

                dist = hamming_dist(m, word)
                if best_dist > dist:
                    best_dist = dist
                    best_word = word
                    best_m = m

            if best_dist > 0 and best_dist < 3:
                # print('')
                # print(best_m, best_word)
                pos = i
                word = best_word
                kpos = pos % 60
                ln = len(word)
                kplm = caesar_cipher(buf[pos:pos+ln], word)

                if kpos+ln > 60: continue
                # print(2)
                #     key = key * 2
                #     key[kpos:kpos+ln] = kplm
                #     key[0:ln] = key[60:60+ln]
                #     key = key[0:60]
                # else:
                should_change = True
                for i in range(0, ln):
                    # print(not used[kpos + i], key[i+kpos] == kplm[i])
                    if kplm[i] not in allchar:
                        should_change = False
                        break
                    elif not used[kpos + i] or key[i+kpos] == kplm[i]:
                        pass
                    else:
                        should_change = False

                # print(3)
                if should_change:
                    print(best_word, best_m)

                    # print(4)
                    key[kpos:kpos+ln] = kplm

                    for i in range(kpos, kpos+ln):
                        used[i] = True

                    k = cacaesar_cipher(buf, key, used)
                    # print(k[pos:pos+ln])
                    # print(word)
                    assert(k[pos:pos+ln] == word)
                    has_changed = True

    # # print(k.count('end'))
    # # print(k.count('ctf'))
    # # print(k.count('CTF'))
    # # print('')

    # k = caesar_cipher(buf, key)

    with open('./out/' + file, 'wb') as f:
        f.write(k)


    print(k[299:310])
    print(len(key))
    print(used)
    print(''.join([ a if b else '.' for a, b in zip(key, used) ]))
    print('')

# allchar = string.ascii_letters + string.punctuation + string.digits
# password = ('').join((choice(allchar) for i in range(randint(60, 60))))
# buf = caesar_cipher(buf, password)
# f = open('./youfool!.exe', 'w')
# buf = f.write(buf)
# f.close()
