# =============================
#   Problem - 706C - Hard Problem
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    lis = list(map(int, input().split()))

    dico = []

    for i in range(n):
        dico.append(input())

    print(dico)

    stdout.write(str(int(n)))

if __name__ == '__main__':
    main()
