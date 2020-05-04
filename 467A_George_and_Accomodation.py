# =============================
#   Problem - 467A - George and Accommodation
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    res = 0
    for i in range(n):
        p, q = map(int, input().split())
        if q - p >= 2:
            res += 1

    stdout.write(str(res))

if __name__ == '__main__':
    main()
