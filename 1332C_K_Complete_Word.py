# =============================
#   Problem - 1332C : K-Complete Word
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout
    from math import floor, ceil

    n = int(input())

    for i in range(n):
        size, k = map(int, input().split())
        word = input()

        example = word[:k]
        res = 0
        # First, check that example is a palyndrome

        for ind in range(floor(k/2)):
            if example[ind] != example[k-ind - 1]:
                res += 1

        sym = ''
        for ind in range(k):
            if ind < ceil(k/2):
                print('ok')
                sym += example[ind]
            else:
                print('hzum')
                sym += example[k - 1 - ind]
        print(sym)

        # Second check that this palydrome is repeated

        track = 0

        for el in word[k:]:
            if el != sym[track]:
                res += 1
            track += 1
            if track == k-1:
                track = 0

        stdout.write(str(res) + '\n')

if __name__ == '__main__':
    main()
