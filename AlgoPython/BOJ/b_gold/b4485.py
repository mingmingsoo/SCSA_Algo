'''
문제 설명
    검정루피 돈잃어
    아 다익스트라네요
'''
import heapq
row = [-1,1,0,0]
col = [0,0,1,-1]
num = 1
ans = []
while True:
    n = int(input())
    if n ==0:
        print("\n".join(ans)) # 요거 한번에 출력으로 변경
        break
    grid = [list(map(int, input().split())) for i in range(n)]

    d = [[125*125*10] * n for i in range(n)]
    d[0][0] = grid[0][0]

    def dijk():
        q = []
        heapq.heappush(q, (grid[0][0],0,0))
        while q:
            cost, r, c = heapq.heappop(q)
            if r == n-1 and c == n-1:
                ans.append(f"Problem {num}: {cost}")
                return
            if cost > d[r][c]:
                continue
            for k in range(4):
                nr = r+row[k]
                nc = c+col[k]
                if not (0<=nr<n and 0<=nc<n):
                    continue
                if d[nr][nc] > cost+ grid[nr][nc]:
                    d[nr][nc] = cost+grid[nr][nc]
                    heapq.heappush(q,(cost+grid[nr][nc],nr,nc))


    dijk()
    num +=1