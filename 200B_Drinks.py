# =============================
#   Problem - 200B - Drinks
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    lis = list(map(int, input().split()))

    res = 0
    for el in lis:
        res += el

    res /= n

    stdout.write(str(res))

if __name__ == '__main__':
    main()
