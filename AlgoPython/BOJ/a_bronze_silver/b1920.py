'''
[구상]
    1. 오름차순 정렬
    2. 이진 탐색
'''


def binary_search(target):
    start = 0
    end = n - 1

    while start <= end:
        middle = (start + end) // 2
        if (arr[middle] == target):
            return 1
        elif (arr[middle] > target):
            end = middle - 1
        else:
            start = middle + 1
    return 0


n = int(input())
arr = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

arr.sort()

for target in find:
    print(binary_search(target))
