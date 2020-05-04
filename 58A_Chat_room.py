# =============================
#   Problem - 58A - Chat room
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = input()
    ind = 0
    hello = 'hello'
    res = 'NO'
    for el in n:
        if el == hello[ind]:
            ind += 1
        if ind == 5:
            res = 'YES'
            break

    stdout.write(res)

if __name__ == '__main__':
    main()
