# =============================
#   Problem - 479A - Expression
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    a = int(input())
    b = int(input())
    c = int(input())

    if a == c == 1:
        res = a + b + c
    elif a == 1:
        res = (a + b) * c
    elif c == 1:
        res = a * (b + c)
    elif b == 1:
        if a < c:
            res = (a + b) * c
        else:
            res = a * (b + c)
    else:
        res = a * b * c

    stdout.write(str(res))

if __name__ == '__main__':
    main()
