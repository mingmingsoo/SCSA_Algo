T = int(input())
for tc in range(T):
    from collections import deque

    start, end = map(int, input().split())

    visited = [False] * 10000
    ans = ""

    q = deque([(start, ans)])
    visited[start] = True

    while q:
        cur, curAns = q.popleft()
        if (cur == end):
            print(curAns)
            break
        mul2 = (cur * 2) % 10000
        minus1 = (cur - 1) % 10000

        strNum = str(f"{cur:04}")
        strL = strNum[1:] + strNum[0]
        strR = strNum[3] + strNum[:3]

        if (not visited[mul2]):
            q.append((mul2, curAns + "D"))
            visited[mul2] = True
        if (not visited[minus1]):
            q.append((minus1, curAns + "S"))
            visited[minus1] = True
        if (not visited[int(strL)]):
            q.append((int(strL), curAns + "L"))
            visited[int(strL)] = True
        if (not visited[int(strR)]):
            q.append((int(strR), curAns + "R"))
            visited[int(strR)] = True