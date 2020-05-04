# =============================
#   Problem - 734A - Anton and Danik
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    matchs = input()

    A = matchs.count('A')
    D = matchs.count('D')

    if A > D:
        res = 'Anton'
    elif A == D:
        res = 'Friendship'
    else:
        res = 'Danik'

    stdout.write(res)

if __name__ == '__main__':
    main()
