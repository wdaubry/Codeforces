# =============================
#   Problem - 133A - HQ9+
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    instruction = input()
    res = 'NO'
    for el in instruction:
        if el == 'H' or el == 'Q' or el == '9':
            res = 'YES'
            break


    stdout.write(str(res))

if __name__ == '__main__':
    main()
