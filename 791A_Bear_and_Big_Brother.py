# =============================
#   Problem - 791A - Bear and Big Brother
#       Python3
#   Author - wdaubry
# =============================
def main():
    from sys import stdout

    a, b = map(int, input().split())
    res = 0
    while a <= b:
        a *= 3
        b *= 2
        res += 1

    stdout.write(str(res))

if __name__ == '__main__':
    main()
