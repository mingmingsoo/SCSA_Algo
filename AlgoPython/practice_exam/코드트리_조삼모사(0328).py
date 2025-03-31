'''
# 코드트리 조삼모사
2025.03.28.금
두번째 풀이(이지만 예전에 풀어봤어서 3번째 풀이)

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 21:31
    문제 종료 21:51

    총 풀이시간 20분
        31~34   : 문제 이해, 초기 주석(3)
        34~39   : combi 설계(5)
        39~45   : 절반만 돌게 (n)C(n//2) 계산 -> 사실 sel[0] != 0 return 과 같은 것.(6)
        45~51   : 이중 포문 돌게해서 점수 계산 설계(6)

  메모리 23 MB
  시간 324 ms

# 문제 풀면서의 기록
문제 설명
    업무 n개가 주어졌을때 어떻게 반띵할래?
    아침 - 저녁 업무 강도 차이를 최소화
구상
    아침에 n//2 고르고 선택 안된 애들이 저녁!
    123/456 이랑
    456/123랑 같은뎅
    그러면 조합 하고 절반만 돌게하장.
    0123
    2301 같은겅
'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

sel = [0] * (n // 2)
ans = 100 * 10 + 1


def combi(sidx, idx):
    global ans
    if sel[0]:
        return
    if sidx == n // 2:
        not_sel = []
        for i in range(n):
            if i not in sel:
                not_sel.append(i)
        # print(sel, not_sel)
        A = B = 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                a, b, x, y = sel[i], sel[j], not_sel[i], not_sel[j]
                A += grid[a][b] + grid[b][a]
                B += grid[x][y] + grid[y][x]
        ans = min(ans,abs(A-B))
        return
    if idx == n:
        return
    sel[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
print(ans)