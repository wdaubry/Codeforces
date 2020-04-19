from math import ceil as c
def invr():
    return map(int, input().split())

n, m, A = invr()

i = c(n/A)
j = c(m/A)

print(i*j)
