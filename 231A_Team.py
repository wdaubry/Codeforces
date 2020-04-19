# =============================
#   Problem - 231A : Team
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    cnt = 0

    for i in range(n):
        lis = (list(map(int, input().split())))
        num = 0;
        for j in lis:
            num += j
        if num >= 2:
            cnt += 1

    stdout.write(str(cnt))

if __name__ == '__main__':
    main()
