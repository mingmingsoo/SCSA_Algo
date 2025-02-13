import math
while True:
    try:
        arr, target = input().split()
    except EOFError:
        break
    target = int(target)
    n = len(arr)
    if (target > math.factorial(n)):
        print(f'{"".join(arr)} {target} = No permutation')
        continue
    sel = [0] * n

    visited = [False] * n
    cnt = 0

    def perm(idx):
        global cnt
        if (cnt > target):
            return
        if (idx == n):
            cnt += 1
            if (cnt == target):
                print(f'{"".join(arr)} {target} = {"".join(sel)}')
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                sel[idx] = arr[i]
                perm(idx + 1)
                visited[i] = False
    perm(0)
