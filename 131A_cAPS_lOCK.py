# =============================
#   Problem - 131A - cAPS lOCK
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    word = input()

    change = True
    for el in word[1:]:
        if not ord('A') <= ord(el) <= ord('Z'):
            change_mode = False

    if change:
        if ord('A') <= ord(word[0]) <= ord('Z'):
            word = word.lower()
        else:
            word = word.capitalize()

    stdout.write(word)

if __name__ == '__main__':
    main()
