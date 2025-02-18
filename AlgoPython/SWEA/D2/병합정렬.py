T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0


    def merge_sort(arr):
        global ans
        # 1. 종료조건
        if len(arr) <= 1:
            return arr

        # 2. left, right 나눠서 각각 정렬 후 합치기
        m = len(arr) // 2
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])

        if (left[-1] > right[-1]):
            ans += 1

        # 3. 합치기
        rlt = []
        l = r = 0
        while l < len(left) and r < len(right):  # 둘 중에 하나는 비어져야,,
            if left[l] < right[r]:
                rlt.append(left[l])
                l += 1
            else:
                rlt.append(right[r])
                r += 1
        # 4. left, right 중 하나만 남음
        return rlt + left[l:] + right[r:]


    lst = merge_sort(arr)
    print(f"#{tc+1} {lst[n // 2]} {ans}")