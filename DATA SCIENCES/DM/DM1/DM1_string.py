import pandas as pd
import numpy as np


# ---------- String ---------------


def donuts(count):
    if count < 10:
        result = 'Number of donuts: ' + str(count)
    else:
        result = 'Number of donuts: many'
    print(result)
    return result


def both_ends(s):
    result = s[0:2] + s[-2:len(s)]
    return result


def fix_start(s):
    premiere = s[0:1]
    reste = s[1:len(s)]
    remplace = reste.replace(premiere, '*')
    resultat = premiere + remplace
    return resultat


def mix_up(a, b):
    sub1 = a[0:2]
    reste1 = a[-(len(a) - len(sub1)):len(a)]
    sub2 = b[0:2]
    reste2 = b[-(len(b) - len(sub1)):len(b)]
    resultat = sub2 + reste1 + ' ' + sub1 + reste2
    return resultat


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


main()
