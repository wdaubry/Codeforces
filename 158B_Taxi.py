# =============================
#   Problem - 158B - Taxi
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout
    from math import ceil

    n = int(input())
    list = map(int, input().split())

    count = [0]*4

    for el in list:
        count[el-1] += 1

    taxi = count[3]
    taxi += count[2]

    count[0] -= count[2]

    if count[0] > 0:
        taxi += ceil(count[0]/4 + count[1]/2)
    else:
        taxi += ceil(count[1]/2)

    stdout.write(str(int(taxi)))

if __name__ == '__main__':
    main()
