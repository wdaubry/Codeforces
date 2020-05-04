# =============================
#   Problem - 1343A : Candies
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

    lis = [1]
    while (lis[len(lis) -1] < 10**9+1):
        lis.append(lis[len(lis) - 1]+(2**(len(lis))))

    for i in range(n):
        inp = int(input())

        for el in lis[1:]:
            if inp%el == 0:
                res = int(inp/el)
                stdout.write(str(res) + '\n')
                break;

if __name__ == '__main__':
    main()
