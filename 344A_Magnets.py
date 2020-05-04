# =============================
#   Problem - 344A - Magnets
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    current = ''
    res = 0
    for i in range(n):
        new = input()
        if new != current:
            current = new
            res += 1

    stdout.write(str(res))

if __name__ == '__main__':
    main()
