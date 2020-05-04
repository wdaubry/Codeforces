# =============================
#   Problem - 4C - Registration system
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    dico = {}

    for i in range(n):
        word = input()
        if word in dico:
            dico[word] += 1
            stdout.write(str(word) + str(dico[word]) + '\n')
        else:
            dico[word] = 0
            stdout.write('OK' + '\n')



if __name__ == '__main__':
    main()
