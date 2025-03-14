'''
루트로 나눈 값+1 까지 나랑 나눠떨어지는 애 있으면 소수아님
'''
import math

N = int(input())


def btk(idx, arr):
    if arr:
        if arr[0] == 1:
            return
        num = int("".join(map(str, arr)))
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                return
    if idx == N:
        print("".join(map(str, arr)))
        return

    for i in (1, 2, 3, 5, 7, 9):
        arr.append(i)
        btk(idx + 1, arr)
        arr.pop()


btk(0, [])
