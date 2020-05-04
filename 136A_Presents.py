# =============================
#   Problem - 136A - Presents
#       Python3
#   Author - wdaubry
# =============================

def main():

    n = int(input())
    lis = map(int, input().split())
    res = [0]*n
    for el, ind in zip(lis, range(n)):
        res[el-1] = ind+1

    print(*res)


if __name__ == '__main__':
    main()
