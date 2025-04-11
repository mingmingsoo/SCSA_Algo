n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

# 부분집합
sel = [0] * n
ans = int(1e9)


def subset(idx):
    global ans
    if idx == n:
        if sel[0] != 1:
            return
        link = []
        start = []
        for i in range(n):
            if sel[i]:
                link.append(i)
            else:
                start.append(i)
        link_score = 0
        start_score = 0

        for i in range(len(link)):
            a = link[i]
            for j in range(i + 1, len(link)):
                b = link[j]
                link_score += grid[a][b]
                link_score += grid[b][a]

        for i in range(len(start)):
            a = start[i]
            for j in range(i + 1, len(start)):
                b = start[j]
                start_score += grid[a][b]
                start_score += grid[b][a]

        diff = abs(start_score - link_score)
        ans = min(ans, diff)

        return

    sel[idx] = 0
    subset(idx + 1)
    sel[idx] = 1
    subset(idx + 1)


subset(0)
print(ans)
