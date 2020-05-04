# =============================
#   Problem - 1030A - In Search of an Easy Problem
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    lis = map(int, input().split())

    res = "EASY"
    for el in lis:
        if el == 1:
            res = "HARD"

    stdout.write(res)

if __name__ == '__main__':
    main()
