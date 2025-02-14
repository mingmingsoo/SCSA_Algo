import sys

input = sys.stdin.readline

n, m = map(int, input().split())
if m < 5:  # 'antic' 조차 못 배우면 0
    print(0)
    sys.exit()

arr = set()
line_list = []

for _ in range(n):
    line = input().rstrip()
    new_line = set(line[4:-4]) - set("antic")  # 'antic' 제거
    arr.update(new_line)
    line_list.append(new_line)

arr = list(arr)  # 리스트로 변환
n = len(arr)
ans = 0


def combi(idx, selected):
    global ans
    if len(selected) == m - 5:  # k-5개의 글자 선택 완료
        count = sum(1 for line in line_list if line <= selected)  # 포함된 단어 개수 카운트
        ans = max(ans, count)
        return

    if idx == n:  # 남은 글자가 없으면 종료
        return

    # 현재 글자 포함
    selected.add(arr[idx])
    combi(idx + 1, selected)
    selected.remove(arr[idx])

    # 현재 글자 미포함
    combi(idx + 1, selected)


combi(0, set())  # 빈 set으로 시작
print(ans)
