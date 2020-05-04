# =============================
#   Problem - 705A - Hulk
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    res = ''
    for i in range(n):
        if i%2 == 0:
            res += 'I hate'
        else:
            res += 'I love'
        if i == n-1:
            res += ' it '
        else:
            res += ' that '

    stdout.write(res)

if __name__ == '__main__':
    main()
