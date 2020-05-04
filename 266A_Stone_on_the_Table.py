# =============================
#   Problem - 266A : Stones on the Table
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    inp = int(input())
    inp2 = input()

    first = ''
    res = 0
    for el in inp2:
        if el == first:
            res += 1
        first = el

    stdout.write(str(res))

if __name__ == '__main__':
    main()
