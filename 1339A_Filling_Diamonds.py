# =============================
#   Problem - 1339A : Filling Diamonds
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

    for i in range(n):
        inp = int(input())
        stdout.write(str(inp) + "\n")

if __name__ == '__main__':
    main()
