# =============================
#   Problem - 116A - Tram
#       Python3
#   Author - wdaubry
# =============================
def main():
    from sys import stdout

    n = int(input())

    people = 0
    max = 0
    for i in range(n):
        out, ins = map(int, input().split())

        people += ins - out

        if people > max:
            max = people

    stdout.write(str(max))

if __name__ == '__main__':
    main()
