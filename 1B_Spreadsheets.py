# =============================
#   Problem - 1B : Spreadsheets
#       Python3
#   Author - wdaubry
# =============================

'''
    For each figure, what change from the different ways to
    cover the figure depends on the position of the vertical
    diamond, there can only be one. So answer is n.
'''
from math import floor

def swap(word, RXCY):
    res = ''
    if not RXCY:
        first = ''
        second = ''
        for el in word:
            if ord('A') <= ord(el) <= ord('Z'):
                first += el
            else:
                second += el

        numb = 0
        for ind in range(len(first)):
            numb += (ord(first[ind])-(ord('A')-1)) * (26**(len(first)-1-ind))

        res = 'R' + second + 'C' + str(numb)
    else:
        first = ''
        second = ''
        second_val = False
        for el in word:
            if el == 'C':
                second_val = True
            elif el == 'R':
                pass
            else:
                if second_val:
                    first += el
                else:
                    second += el

        part_1 = ''
        numb = int(first)
        for i in range(4, -1 , -1):
            div = floor(numb/(26**i))
            #(div)
            if (div != 0) or (i == 0):
                numb = numb%(26**i)
                if numb == 0:
                    if div == 0:
                        part_1 += chr(ord('Z'))
                    else:
                        part_1 += chr(div + ord('A') - 2)
                else:
                    part_1 += chr(div + ord('A') - 1)


        res = part_1 + second

    return res

def main():
    from sys import stdout

    n = int(input())

    for i in range(n):
        word = input()
        RXCY = False

        first = ''
        second = ''

        if word[0] == 'R':
            if not (ord('A') <= ord(word[1]) <= ord('Z')):
                numb_meet = False
                for j in range(1, len(word)):
                    if (ord('0') <= ord(word[j]) <= ord('9')):
                        numb_meet = True
                    elif numb_meet and word[j] == 'C':
                        RXCY = True

        res = swap(word, RXCY)

        stdout.write(res + "\n")

if __name__ == '__main__':
    main()
