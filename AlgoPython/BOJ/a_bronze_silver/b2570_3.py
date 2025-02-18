T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))


    def partition(left, right):
        pivot = arr[left]  # 처음값
        L, R = left + 1, right
        while L <= R:
            while L <= R and arr[L] <= pivot:
                L += 1
            while arr[R] > pivot:
                R -= 1
            if L < R:
                arr[L], arr[R] = arr[R], arr[L]

        arr[left], arr[R] = arr[R], arr[left]

        return R  # 피봇위치


    def quick_sort(left, right):
        if left < right:
            pivot = partition(left, right)
            quick_sort(left, pivot - 1)
            quick_sort(pivot + 1, right)


    quick_sort(0, n - 1)
    print(f"#{tc+1} {arr[n // 2]}")