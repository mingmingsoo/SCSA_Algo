
'''
# 코드트리 조삼모사
2025.03.29.금
두번째 풀이(예전에 풀어봄)

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 19:35
    문제 종료 19:58

    총 풀이시간 23분
        35~43   : 탑다운 설계 세로는 가로를 전치해서 계산한 것!(8)
        43~58   : is_ok 함수 설계(15)

  메모리 52 MB
  시간 17 ms

'''

n, length = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
gridT = map(list, zip(*grid))

ans = 0


def is_ok(row):
    idx = 0
    karo = 0
    height = row[0]

    while idx < n:
        if row[idx] == height:
            karo += 1
            idx += 1
        elif row[idx] == height + 1:  # 전보다 한 칸 높아
            if karo >= length:
                height += 1
                karo = 0
            else:
                return False
        elif row[idx] == height - 1:  # 전보다 한 칸 낮아
            if idx + length >= n + 1:  # 길이가 부족하넹
                return False
            for x in range(idx, idx + length):
                if row[x] != height - 1:
                    return False
            # 여까지 왔으면 됐음
            idx += length
            karo = 0
            height -= 1
        else:
            return False

    return True


for row in grid:
    if is_ok(row):
        ans += 1

for row in gridT:
    if is_ok(row):
        ans += 1

print(ans)
