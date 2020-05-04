# =============================
#   Problem - 1338A : Powered Addition
#       Python3
#   Author - wdaubry
# =============================

def biggest_power(x):
    i = 0
    while(2**i <= x):
        i += 1
    return i


def main():
    from sys import stdout

    tests = int(input())

    for i in range(tests):
        cnt_max = 0

        n = int(input())
        lis = list(map(int, input().split()))
        max = lis[0]
        min = lis[0]
        for ind in range(1, n):
            cnt = 0
            if lis[ind] < max:
                if min > lis[ind]:
                    min = lis[ind]
            else:
                cnt = biggest_power(max - min)
                max = lis[ind]
                min = lis[ind]
                if cnt > cnt_max:
                    cnt_max = cnt

            if (ind == n-1) and (max - min) > 0:

                cnt = biggest_power(max - min)
                if cnt > cnt_max:
                    cnt_max = cnt

        stdout.write(str(cnt_max) + "\n")

if __name__ == '__main__':
    main()
