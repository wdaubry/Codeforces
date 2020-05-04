# =============================
#   Problem - 69A - Young Physicist
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    sum = [0] * 3
    for i in range(n):
        val = list(map(int, input().split()))
        for j in range(3):
            sum[j] += val[j]

    if sum[0] == sum[1] == sum[2] == 0:
        res = 'YES'
    else:
        res = 'NO'

    stdout.write(res)

if __name__ == '__main__':
    main()
