# =============================
#   Problem - 935A - Fafa and his Company
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    res = 0
    for i in range(1, n):
        if (n - i)/i%1 == 0:
            res += 1

    stdout.write(str(res))

if __name__ == '__main__':
    main()
