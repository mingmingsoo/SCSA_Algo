# T = 100
# for tc in range(T):
#     n, m = map(int, input().split())
#
#     row = [0, 1, 0, -1]
#     col = [1, 0, -1, 0]
#     visited = [[False] * m for i in range(n)]
#
#     r = 0
#     c = 0
#     d = 0
#     cnt = 0
#     num = 1
#     while num < n * m:
#         visited[r][c] = True
#         if not (0 <= r + row[d] < n and 0 <= c + col[d] < m) or visited[r + row[d]][c + col[d]]:
#             d = (d + 1) % 4
#             cnt += 1
#
#         nr = r + row[d]
#         nc = c + col[d]
#
#         r = nr
#         c = nc
#         num += 1
#     print(cnt)
#     print(r + 1, c + 1)

T = 100
for tc in range(T):
    n, m = map(int, input().split())
    # print(n, m)
    if (n % 2 == 0 and m >= n):
        print(n // 2 + 1, n // 2)
    elif (n % 2 == 0 and m < n):
        if (m % 2 == 0):
            print(m - (m - 1) // 2, m // 2)
        else:
            print(m // 2 + 1 + n - m, m // 2 + 1)


    elif (n % 2 != 0 and m >= n):
        print(n // 2 + 1, m//2+1)
    elif (n % 2 != 0 and m < n):
        if (m % 2 == 0):
            print(m * 2 - 1)
            print(m - (m - 1) // 2, m // 2)
        else:
            print(m * 2 - 1)
            print(m // 2 + 1 + n - m, m // 2 + 1)
