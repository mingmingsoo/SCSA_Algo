'''
문제설명
    씨앗 3개
    다른 꽃이랑 닿으면 주금 ㅠㅠ 범위 벗어나도 주금
    가장  싼 화단에! 근데 5칸!
구상
    무조건 3개 꽃이 필 수 있는 맵 크기이다.
    일단 화단 가격 미리 계산한다
    그리고 범위 내에서 가능하면 꽃 피운다!
    btk
틀린이유
    ans = 200 * 5  + 1
    이 아니라
    ans = 200 * 5 * 3 + 1임!!
    꽃 3개
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
money = [[0] * n for i in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        money[i][j] = grid[i][j] + grid[i - 1][j] + grid[i + 1][j] + grid[i][j - 1] + grid[i][j + 1]

visited = [[False] * n for i in range(n)]
ans = 200 * 5 * 3 + 1


def btk(idx, cost):
    global ans
    if cost >= ans:
        return
    if idx == 3:
        ans = min(ans, cost)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if visited[i][j] == visited[i - 1][j] == visited[i + 1][j] == visited[i][j - 1] == visited[i][
                j + 1] == False:
                visited[i][j] = visited[i - 1][j] = visited[i + 1][j] = visited[i][j - 1] = visited[i][
                    j + 1] = True
                btk(idx + 1, cost + money[i][j])
                visited[i][j] = visited[i - 1][j] = visited[i + 1][j] = visited[i][j - 1] = visited[i][
                    j + 1] = False


btk(0, 0)
print(ans)
