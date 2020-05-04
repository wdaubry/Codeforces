# =============================
#   Problem - 580A : Kefa and First Steps
#       Python3
#   Author - wdaubry
# =============================

'''
    For each figure, what change from the different ways to
    cover the figure depends on the position of the vertical
    diamond, there can only be one. So answer is n.
'''

def main():
    from sys import stdout

    n = int(input())
    lis = list(map(int, input().split()))

    res = 0
    cnt = 0
    num = 0
    for el in lis:
        if el >= num:
            cnt += 1
            num = el
        else:
            if res < cnt:
                res = cnt
            cnt = 1
            num = el
    if res < cnt:
        res = cnt

    stdout.write(str(res) + "\n")

if __name__ == '__main__':
    main()
