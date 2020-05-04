# =============================
#   Problem - 677A - Vanya and Fence
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n, h = map(int, input().split())
    lis = list(map(int, input().split()))

    count = 0

    for el in lis:
        if el > h:
            count += 2
        else:
            count += 1

    stdout.write(str(count))

if __name__ == '__main__':
    main()
