# =============================
#   Problem - 112A : Petya and Strings
#       Python3
#   Author - wdaubry
# =============================


def main():
    from sys import stdout

    first = input()
    second = input()

    space = ord('a') - ord('A')
    start_cap = ord('A')
    end_cap = ord('Z')

    res = 0

    for i in range(len(first)):
        first_i = ord(first[i])
        second_i = ord(second[i])
        if start_cap <= first_i <= end_cap:
            first_i += space
        if start_cap <= second_i <= end_cap:
            second_i += space
        if first_i < second_i:
            res = -1
            break
        if first_i > second_i:
            res = 1
            break

    stdout.write(str(res))

if __name__ == '__main__':
    main()
