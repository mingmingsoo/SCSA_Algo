'''
# 제출횟수: 6회
# 실행시간: 148ms
# 메모리: 127052 KB

답이 되는 거리를 이분탐색
만약 간격이 middle보다 작으면 그 돌을 없애보고,
m개만큼 제거가 되면 start 늘려보기
아니면 값 조정 필요 end 줄이기
'''


def isOk(middle):
    remove = 0
    arr = arr_origin[:]

    for i in range(len(arr)):
        if arr[i] < middle:
            if remove < m:
                remove += 1
                arr[i + 1] += arr[i]
            else:
                return False
    return True


end, n, m = map(int, input().split())
tmp = [int(input()) for i in range(n)]
tmp.sort()
tmp.insert(0, 0)
tmp.append(end)
arr = []
for i in range(len(tmp) - 1):
    arr.append(tmp[i + 1] - tmp[i])
# print(arr)

start = 0
ans = 0
arr_origin = arr[:]

while start <= end:

    middle = (start + end) // 2
    if isOk(middle):  # 가능하다면 늘려보기
        ans = middle
        start = middle + 1
    else:  # 안되면 줄이기
        end = middle - 1

print(ans)
