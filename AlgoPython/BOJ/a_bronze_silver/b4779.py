import sys

while True:
    try:
        n = int(input())
        n = 3 ** n
        arr = ["-"] * (n)


        def btk(n, left, right):
            if n == 1:
                return
            for i in range(left + n // 3, left + n // 3 * 2):
                arr[i] = " "
            btk(n // 3, left, left + n // 3)
            btk(n // 3, right - n // 3, right)


        btk(n, 0, n)
        print("".join(arr))
    except EOFError:
        break
