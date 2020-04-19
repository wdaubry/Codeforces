# =============================
#   Problem - 263A : Beautiful Matrix
#       Python3
#   Author - wdaubry
# =============================
import numpy as np

def main():
    from sys import stdout

    zeros = [0]*5

    res = 0
    for i in range(-2, 3):
        line = list(map(int, raw_input().split()))
        if not np.array_equal(line, zeros):
            res += abs(i)
            for j in range(5):
                if line[j] == 1:
                    res += abs(j-2)

    stdout.write(str(res))

if __name__ == '__main__':
    main()
