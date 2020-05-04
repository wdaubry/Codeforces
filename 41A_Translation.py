# =============================
#   Problem - 41A - Translation
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    berland = input()
    birland = input()

    res = 'YES'
    for i,j in zip(berland, birland[::-1]):
        if i != j:
            res = 'NO'
            break

    stdout.write(res)

if __name__ == '__main__':
    main()
