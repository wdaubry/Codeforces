# =============================
#   Problem - 158A : Next Round
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    inp = input()

    str_inp = [ord(c) for c in inp]

    #A, E, I, O, U, Y & a, e, i, o, u, y
    voy_min = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u'), ord('y')]
    voy_max = [ord('A'), ord('E'), ord('I'), ord('O'), ord('U'), ord('Y')]
    cap_min = ord('A')
    cap_max = ord('Z')
    space_cap = ord('a') - ord('A')

    final_str = ''
    for numb in str_inp:
        if not numb in voy_min and not numb in voy_max:
            final_str += '.'
            if cap_min <= numb <= cap_max:
                final_str += chr(numb + space_cap)
            else:
                final_str += chr(numb)


    stdout.write(final_str)

if __name__ == '__main__':
    main()
