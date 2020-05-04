# =============================
#   Problem - 271A - Beautiful Year
#       Python3
#   Author - wdaubry
# =============================

def isdifferent(word):
    lis = []
    for el in word:

        if el in lis:
            return False
        else:
            lis.append(el)

    return True


def main():
    from sys import stdout

    year = str(int(input()) + 1)

    while not isdifferent(year):
        year = str(int(year) + 1)

    stdout.write(year)

if __name__ == '__main__':
    main()
