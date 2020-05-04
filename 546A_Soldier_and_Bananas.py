# =============================
#   Problem - 546A - Soldier and Bananas
#       Python3
#   Author - wdaubry
# =============================

def sum(n):
    if n%2 == 0:
        return int((n+1)*(n/2))
    else:
        return int((n+1)*(n/2.0))

def main():
    from sys import stdout

    k, n, w = map(int, input().split())

    price = sum(w)
    money = price*k

    if money >= n:
        res = money - n
    else:
        res = 0

    stdout.write(str(res))

if __name__ == '__main__':
    main()
