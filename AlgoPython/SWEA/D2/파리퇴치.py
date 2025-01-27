# T = int(input())
#
# for tc in range(T):
#     n, m = map(int, input().split())
#     grid = [list(map(int, input().split())) for i in range(n)]
#     ans = -1
#     for i in range(0, n - m + 1):
#         for j in range(0, n - m + 1):
#             # 시작점 설정
#             sum = 0
#             for r in range(i, i + m):
#                 for c in range(j, j + m):
#                     sum += grid[r][c]
#             ans = max(sum, ans)
#
#     print(f"#{tc+1} {ans}")
#

# 누적합으로 풀기
T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = -1
    for i in range(0, n - m + 1):
        for j in range(0, n - m + 1):
            # 시작점 설정
            sum = 0
            for r in range(i, i + m):
                for c in range(j, j + m):
                    sum += grid[r][c]
            ans = max(sum, ans)

    print(f"#{tc+1} {ans}")

