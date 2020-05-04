# =============================
#   Problem - 266B - Queue at the School
#       Python3
#   Author - wdaubry
# =============================
def main():
    from sys import stdout

    n, t = map(int, input().split())
    line = input()
    new_line = line
    if n != 1:
        for i in range(t):
            line = new_line
            new_line = ''
            pass_ = False
            for ind in range(len(line) - 1):
                if pass_:
                    if ind == len(line) - 2:
                        new_line += line[ind+1]
                    pass_ = False
                else:
                    if line[ind] == 'B' and line[ind+1] == 'G':
                        new_line += 'GB'
                        pass_ = True
                    else:
                        if ind == len(line) - 2:
                            new_line += line[ind] + line[ind+1]
                        else:
                            new_line += line[ind]
    else:
        new_line = line

    stdout.write(new_line)

if __name__ == '__main__':
    main()
