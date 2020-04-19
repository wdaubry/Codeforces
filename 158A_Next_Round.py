# =============================
#   Problem - 158A : Next Round
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n, k = map(int, input().split())

    lis = list(map(int, input().split()))

    cnt = 0

    for numb in lis:
        if numb >= lis[k-1] and numb > 0:
            cnt += 1

    stdout.write(str(cnt))

if __name__ == '__main__':
    main()
