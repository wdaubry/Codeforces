# =============================
#   Problem - 160A - Twins
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    lis = list(map(int, input().split()))
    sum = 0
    for el in lis:
        sum += el

    money = 0
    ind = 0
    while money <= sum/2:
        money += max(lis)
        ind += 1
        lis.remove(max(lis))

    stdout.write(str(ind))

if __name__ == '__main__':
    main()
