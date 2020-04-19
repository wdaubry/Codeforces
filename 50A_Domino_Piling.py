# =============================
#   Problem - 50A : Domino Piling
#       Python3
#   Author - wdaubry
# =============================
from math import floor

def main():
    from sys import stdout

    m, n = map(int, input().split())

    total = m*n
    res = floor(total/2)

    stdout.write(str(res))

if __name__ == '__main__':
    main()
