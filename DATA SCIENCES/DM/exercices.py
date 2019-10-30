import pandas as pd
import numpy as np


# ---------- String ---------------

# A. donuts
def donuts(count):
    if count < 10:
        result = 'Number of donuts: ' + str(count)
    else:
        result = 'Number of donuts: many'
    print(result)
    return result


# B. both_ends
def both_ends(s):
    result = s[0:2] + s[-2:len(s)]
    return result


# B. fix_start
def fix_start(s):
    premiere = s[0:1]
    reste = s[1:len(s)]
    remplace = reste.replace(premiere, '*')
    resultat = premiere + remplace
    return resultat


# B. mix_up
def mix_up(a, b):
    sub1 = a[0:2]
    reste1 = a[-(len(a) - len(sub1)):len(a)]
    sub2 = b[0:2]
    reste2 = b[-(len(b) - len(sub1)):len(b)]
    resultat = sub2 + reste1 + ' ' + sub1 + reste2
    return resultat


# ---------- List ---------------

def match_ends(words):
    count = 0
    for w in words:
        if len(w) >= 2 and w[0:1] == w[-1:len(w)]:
            count = count + 1
    return count


def front_x(words):
    listx = []
    listy = []
    for w in words:
        if w[0:1] == 'x':
            listx.append(w)
        else:
            listy.append(w)
    listx.sort()
    listy.sort()
    listx.extend(listy)
    return listx


def MyFn(tuple):
    return tuple[len(tuple) - 1]


def sort_last(tuples):
    return sorted(tuples, key=MyFn)


# -------------------------------------


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

    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


main()
