'''
'''
from collections import deque

n = int(input())

arr = list(map(int, input().split()))
ans = 0

q = deque([(arr, 0)])
visited = set()
while q:
    lst, cnt = q.popleft()
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] <= 0:
            lst.pop(i)
    is_end = True
    for num in lst:
        if num > 0:
            is_end = False
            break
    if is_end:
        ans = cnt
        break
    if len(lst) == 3:
        if (lst[0] - 9, lst[1] - 3, lst[2] - 1) not in visited:
            q.append(([lst[0] - 9, lst[1] - 3, lst[2] - 1], cnt + 1))
            visited.add((lst[0] - 9, lst[1] - 3, lst[2] - 1))

        if (lst[0] - 9, lst[1] - 1, lst[2] - 3) not in visited:
            q.append(([lst[0] - 9, lst[1] - 1, lst[2] - 3], cnt + 1))
            visited.add((lst[0] - 9, lst[1] - 1, lst[2] - 3))

        if (lst[0] - 3, lst[1] - 9, lst[2] - 1) not in visited:
            q.append(([lst[0] - 3, lst[1] - 9, lst[2] - 1], cnt + 1))
            visited.add((lst[0] - 3, lst[1] - 9, lst[2] - 1))

        if (lst[0] - 3, lst[1] - 1, lst[2] - 9) not in visited:
            q.append(([lst[0] - 3, lst[1] - 1, lst[2] - 9], cnt + 1))
            visited.add((lst[0] - 3, lst[1] - 1, lst[2] - 9))

        if (lst[0] - 1, lst[1] - 9, lst[2] - 3) not in visited:
            q.append(([lst[0] - 1, lst[1] - 9, lst[2] - 3], cnt + 1))
            visited.add((lst[0] - 1, lst[1] - 9, lst[2] - 3))

        if (lst[0] - 1, lst[1] - 3, lst[2] - 9) not in visited:
            q.append(([lst[0] - 1, lst[1] - 3, lst[2] - 9], cnt + 1))
            visited.add((lst[0] - 1, lst[1] - 3, lst[2] - 9))

    if len(lst) == 2:
        if (lst[0] - 9, lst[1] - 3) not in visited:
            q.append(([lst[0] - 9, lst[1] - 3], cnt + 1))
            visited.add((lst[0] - 9, lst[1] - 3))
        if (lst[0] - 3, lst[1] - 9) not in visited:
            q.append(([lst[0] - 3, lst[1] - 9], cnt + 1))
            visited.add((lst[0] - 3, lst[1] - 9))

    if len(lst) == 1:
        if (lst[0] - 9) not in visited:
            q.append(([lst[0] - 9], cnt + 1))
            visited.add((lst[0] - 9))
print(ans)
