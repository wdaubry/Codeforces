# =============================
#   Problem - 977A - Wrong Substraction
#       Python3
#   Author - wdaubry
# =============================
def main():
    from sys import stdout

    n, k = map(int, input().split())

    for i in range(k):
        if n%10 == 0:
            n /= 10
        else:
            n -= 1

    stdout.write(str(int(n)))

if __name__ == '__main__':
    main()
