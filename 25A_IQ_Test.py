# =============================
#   Problem - 25A - IQ Test
#       Python3
#   Author - wdaubry
# =============================

def main():
    from sys import stdout

    n = int(input())
    lis = list(map(int, input().split()))

    even, even_numb = 0, 0
    odd, odd_numb = 0, 0
    for i in range(n):
        if lis[i]%2 == 0:
            even += 1
            even_numb += i
        else:
            odd += 1
            odd_numb += i

    if even>odd:
        res = odd_numb
    else:
        res = even_numb

    stdout.write(str(res + 1))

if __name__ == '__main__':
    main()
