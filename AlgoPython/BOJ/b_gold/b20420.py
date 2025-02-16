'''
갈수 있는 방향을 제외하고
추가
'''
import heapq
import sys
input = sys.stdin.readline

n, m, card = map(int, input().split())
grid = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(m):
        grid[i][j] = "URDL".index(grid[i][j])
ans = "No"
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def bfs(sr, sc, er, ec):
    global ans
    q = []
    visited = set()
    heapq.heappush(q, (0, sr, sc, grid[sr][sc], card, card))
    visited.add((sr, sc, grid[sr][sc], card, card))
    if card > 1:
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 2) % 4, card, card - 2))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 3) % 4, card, card - 3))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 2 + 4) % 4, card - 2, card))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 3 + 4) % 4, card - 3, card))
        visited.add((sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        visited.add((sr, sc, (grid[sr][sc] + 2) % 4, card, card - 2))
        visited.add((sr, sc, (grid[sr][sc] + 3) % 4, card, card - 3))
        visited.add((sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
        visited.add((sr, sc, (grid[sr][sc] - 2 + 4) % 4, card - 2, card))
        visited.add((sr, sc, (grid[sr][sc] - 3 + 4) % 4, card - 3, card))

    elif card > 1:
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 2) % 4, card, card - 2))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 2 + 4) % 4, card - 2, card))
        visited.add((sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        visited.add((sr, sc, (grid[sr][sc] + 2) % 4, card, card - 2))
        visited.add((sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
        visited.add((sr, sc, (grid[sr][sc] - 2 + 4) % 4, card - 2, card))
    elif card > 0:
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        heapq.heappush(q, (0, sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
        visited.add((sr, sc, (grid[sr][sc] + 1) % 4, card, card - 1))
        visited.add((sr, sc, (grid[sr][sc] - 1 + 4) % 4, card - 1, card))
    while q:
        location, r, c, d, left, right = heapq.heappop(q)
        # print(location, r, c,"URDL"[d], left, right)
        if r == er and c == ec:
            ans = "Yes"
            return
        nr = r + row[d]
        nc = c + col[d]
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        next_d = grid[nr][nc]
        next_lo = -(nr * n + nc)

        if (nr, nc, next_d, left, right) not in visited:
            heapq.heappush(q, (next_lo, nr, nc, next_d, left, right))
            visited.add((nr, nc, next_d, left, right))
        if left > 2:
            if (nr, nc, (next_d - 1 + 4) % 4, left - 1, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
                visited.add((nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
            if (nr, nc, (next_d - 2 + 4) % 4, left - 2, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 2 + 4) % 4, left - 2, right))
                visited.add((nr, nc, (next_d - 2 + 4) % 4, left - 2, right))
            if (nr, nc, (next_d - 3 + 4) % 4, left - 3, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 3 + 4) % 4, left - 3, right))
                visited.add((nr, nc, (next_d - 3 + 4) % 4, left - 3, right))
        elif left > 1:
            if (nr, nc, (next_d - 1 + 4) % 4, left - 1, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
                visited.add((nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
            if (nr, nc, (next_d - 2 + 4) % 4, left - 2, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 2 + 4) % 4, left - 2, right))
                visited.add((nr, nc, (next_d - 2 + 4) % 4, left - 2, right))
        elif left > 0:
            if (nr, nc, (next_d - 1 + 4) % 4, left - 1, right) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
                visited.add((nr, nc, (next_d - 1 + 4) % 4, left - 1, right))
        if right > 2:
            if (nr, nc, (next_d + 1) % 4, left, right - 1) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 1) % 4, left, right - 1))
                visited.add((nr, nc, (next_d + 1) % 4, left, right - 1))
            if (nr, nc, (next_d + 2) % 4, left, right - 2) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 2) % 4, left, right - 2))
                visited.add((nr, nc, (next_d + 2) % 4, left, right - 2))
            if (nr, nc, (next_d + 3) % 4, left, right - 3) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 3) % 4, left, right - 3))
                visited.add((nr, nc, (next_d + 3) % 4, left, right - 3))

        elif right > 1:
            if (nr, nc, (next_d + 1) % 4, left, right - 1) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 1) % 4, left, right - 1))
                visited.add((nr, nc, (next_d + 1) % 4, left, right - 1))
            if (nr, nc, (next_d + 2) % 4, left, right - 2) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 2) % 4, left, right - 2))
                visited.add((nr, nc, (next_d + 2) % 4, left, right - 2))
        elif right > 0:
            if (nr, nc, (next_d + 1) % 4, left, right - 1) not in visited:
                heapq.heappush(q, (next_lo, nr, nc, (next_d + 1) % 4, left, right - 1))
                visited.add((nr, nc, (next_d + 1) % 4, left, right - 1))


bfs(0, 0, n - 1, m - 1)
print(ans)
