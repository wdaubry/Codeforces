# =============================
#   Problem - 520B : Two Buttons
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n, m = map(int, input().split())

    res = 0
    while(n != m):
        if n >= m:
            res += n-m
            n = m
        else:
            if m%2 == 1:
                m += 1
                res += 1
            m = m/2
            res += 1

    stdout.write(str(int(res)))

if __name__ == '__main__':
    main()
