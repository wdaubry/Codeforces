# =============================
#   Problem - 110A - Nearly Lucky Number
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    numb = input()

    count = 0
    for el in numb:
        if el == '4' or el == '7':
            count += 1

    res = 'YES'

    for el in str(count):
        if el != '4' and el != '7':
            res = 'NO'

    stdout.write(res)

if __name__ == '__main__':
    main()
