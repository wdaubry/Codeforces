# =============================
#   Problem - 37A : Towers
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

    lis_2 = [0] * 1001
    sum = 0
    for el in lis:
        if lis_2[el] == 0:
            sum += 1
        lis_2[el] += 1


    stdout.write(str(max(lis_2)) + ' ' + str(sum))

if __name__ == '__main__':
    main()
