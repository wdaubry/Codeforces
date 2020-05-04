# =============================
#   Problem - 455A - Boredom
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    lis = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if lis[i]%2 == 0:
            even += lis[i]
        else:
            odd += lis[i]
    if even >= odd:
        res = even
    else:
        res = odd

    stdout.write(str(res))

if __name__ == '__main__':
    main()
