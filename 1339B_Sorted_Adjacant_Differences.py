# =============================
#   Problem - 1339B : Sorted Adjacent Differences
#       Python3
#   Author - wdaubry
# =============================

def dist(a, b):
    return abs(a-b)

def main():
    from sys import stdout

    tests = int(input())

    for i in range(tests):
        n = int(input())
        lis = list(map(int, input().split()))
        val = lis[0]
        for ind in range(1, n):



            val = lis[ind]

        stdout.write(str(cnt_max) + "\n")

if __name__ == '__main__':
    main()
