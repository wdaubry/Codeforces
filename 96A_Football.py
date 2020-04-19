# =============================
#   Problem - 96A : Football
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    inp = input()

    cnt = 0
    res = 'NO'
    j = ''
    for i in inp:
        if j == i:
            cnt += 1
        else:
            cnt = 0
        if cnt == 6:
            res = 'YES'
            break
        else:
            j = i

    stdout.write(str(res))

if __name__ == '__main__':
    main()
