# =============================
#   Problem - 263A : Beautiful Matrix
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    res = 0
    for i in range(-2, 3):
        line = list(map(int, input().split()))
        if not (line[0] == line[1] == line[2] == line[3] == line[4]):
            res += abs(i)
            for j in range(5):
                if line[j] == 1:
                    res += abs(j-2)


    stdout.write(str(res))

if __name__ == '__main__':
    main()
