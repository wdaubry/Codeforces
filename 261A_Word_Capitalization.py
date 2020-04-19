# =============================
#   Problem - 261A : Word Capitalization
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    inp = input()

    start_min = ord('a')
    end_min = ord('z')
    space = ord('a') - ord('A')

    if start_min <= ord(inp[0]) <= end_min:
        res = chr(ord(inp[0]) - space) + inp[1:]
    else:
        res = inp

    stdout.write(str(res))

if __name__ == '__main__':
    main()
