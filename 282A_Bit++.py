# =============================
#   Problem - 282A : Bit++
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())

    add_list = ['++X', '+X+', 'X++']
    sub_list = ['--X', '-X-', 'X--']
    x = 0
    for i in range(n):
        inp = input()
        if inp in add_list:
            x += 1
        elif inp in sub_list:
            x -= 1

    stdout.write(str(x))

if __name__ == '__main__':
    main()
