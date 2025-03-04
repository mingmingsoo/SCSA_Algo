# 엔퀸
# 대각선 못놔
# 같은 열 못놔

n = int(input())
ans = 0


def nqueen(jdx):
    global ans
    if jdx == n:
        ans += 1
        return

    for k in range(n):
        if not row[k] and not diag1[jdx + k] and not diag2[jdx - k]:
            row[k] = diag1[jdx + k] = diag2[jdx - k] = True
            nqueen(jdx + 1)
            row[k] = diag1[jdx + k] = diag2[jdx - k] = False


row = [False] * (n)
diag1 = [False] * (2 * n)
diag2 = [False] * (2 * n)
nqueen(0)
print(ans)
