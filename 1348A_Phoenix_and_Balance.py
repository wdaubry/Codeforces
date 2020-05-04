# =============================
#   Problem - 1348A - Phoenix and Balance
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    t = int(input())
    for i in range(t):
        n = int(input())
        if i == 0:
            res = 2
        else:
            res = 6

        stdout.write(str(res) + '\n')

if __name__ == '__main__':
    main()
