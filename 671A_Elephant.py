# =============================
#   Problem - 671A - Elephant
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    res = n//5
    if n%5 !=0:
        res += 1

    stdout.write(str(int(res)))

if __name__ == '__main__':
    main()
