'''
# 코드트리 병원거리 최소화 하기
2025.03.29.토
두번째 풀이(녹화 버튼 늦게 누름 이슈)

# 문제 풀고 나서 기록
    제출 횟수 1회

  메모리 17 MB
  시간 68 ms

  디버깅 내용:
    1. 병원 거리의 합은 각 사람들마다 가장 가까운 병원의 거리들의 합임!! 전체 합이아니다
        -> 수정

# 문제 풀면서 기록
m개 선택 사람들과의 거리 최소
사람들 위치는 미리 담겠다.
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

arr = []
peoples = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            arr.append((i, j))
        if grid[i][j] == 1:
            peoples.append((i, j))

sel = [0] * m
ans = int(1e9)


def combi(sidx, idx):
    global ans
    if sidx == m:
        sm = 0
        for pr, pc in peoples:
            smi = int(1e9)
            for r, c in sel:
                smi = min(abs(r - pr) + abs(c - pc), smi)
            sm += smi
        ans = min(ans, sm)

        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
print(ans)
