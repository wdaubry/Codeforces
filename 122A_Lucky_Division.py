# =============================
#   Problem - 122A - Lucky Division
#       Python3
#   Author - wdaubry
# =============================

def check_lucky(n):
    res = True
    for el in str(n):
        if el != '4' and el != '7':
            res = False
    return res
def main():
    from sys import stdout

    n = int(input())
    res = 'NO'

    if check_lucky(n):
        res = 'YES'
    else:
        for i in range(1, n):
            if check_lucky(i):
                if n%i == 0:
                    res = 'YES'
                    break

    stdout.write(res)

if __name__ == '__main__':
    main()
