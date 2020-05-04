# =============================
#   Problem - 59A - Word
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    word = input()

    lower = 0
    upper = 0

    for el in word:
        if ord('A') <= ord(el) <= ord('Z'):
            upper += 1
        else:
            lower += 1

    if lower >= upper:
        word = word.lower()
    else:
        word = word.upper()

    stdout.write(str(word))

if __name__ == '__main__':
    main()
