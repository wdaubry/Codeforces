# =============================
#   Problem - 236 : Boy or Girl
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    tex = input()

    lis = []

    for chr in tex:
        if chr not in lis:
            lis.append(chr)

    if len(lis)%2 == 0:
        res = "CHAT WITH HER!
    else:
        res = "IGNORE HIM!"

    stdout.write(str(res))

if __name__ == '__main__':
    main()
