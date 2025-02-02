T = int(input())
for tc in range(T):
    from collections import deque

    mod = 10000
    start, end = map(int, input().split())

    q = deque([(start, "")])
    visited = [False] * mod
    while q:
        cur, ans = q.popleft()
        if (cur == end):
            print(ans)
            break
        curStr = str(f"{cur:04}")
        leftStr = int(curStr[1:] + curStr[0])
        rightStr = int(curStr[-1] + curStr[:3])
        if (not visited[(2 * cur) % 10000]):
            q.append(((2 * cur) % 10000, ans + "D"))
            visited[(2 * cur) % 10000] = True
        if (not visited[(cur - 1) % 10000]):
            q.append(((cur - 1) % 10000, ans + "S"))
            visited[(cur - 1) % 10000] = True
        if (not visited[leftStr]):
            q.append((leftStr, ans + "L"))
            visited[leftStr] = True
        if (not visited[rightStr]):
            q.append((rightStr, ans + "R"))
            visited[rightStr] = True