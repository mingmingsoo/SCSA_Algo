'''
# 코드트리 돌아가는 팔각의자
2025.03.29.토
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회(오타..)
    문제 시작 20:07
    1차 제출  20:24
    문제 종료 20:31


    총 풀이시간 24분
        07~12   : 문제 이해, 초기 주석(3)
        12~16   : 탑다운 설계(4)
        16~24   : is_rotation, rotation 함수 설계
        24~31   : 틀려서 디버깅
                    아차차 오타 발견..

  메모리 23 MB
  시간 324 ms

    회고
        1. 틀린 이유
            light_dir = grid[i][6] 이 아니라
            light_dir = grid[i][2] 임
            정신차려!!!!!!!!!!
        2. 저번풀이와 다르게 회전이므로 deque 2차원 배열을 사용!


문제 설명
    회전 번호/ 회전 방향이 주어졌을 때
    연쇄적으로 회전이 일어나는지 확인
    마주보는 방향이 지역이 다르면 회전 가능
                        같으면 불가능 -> 연쇄적으로 일어날 때 방향은 반대가 됨.

필요한 함수
    is_rotate() : 몇 번 의자가 회전하는지 확인
    rotate() : 위 기반 회전

필요한 변수
    rotate_arr : 회전 여부 boolean
    dir_arr : 방향 int
'''
from collections import deque

grid = [deque(map(int, input())) for i in range(4)]
order_num = int(input())


def is_rotation():
    # 내 기준 왼쪽
    left_dir = grid[idx][6]
    rd = -d
    for i in range(idx - 1, -1, -1):
        if grid[i][2] != left_dir:
            rotate_arr[i] = True
            dir_arr[i] = rd
            rd *= -1
            left_dir = grid[i][6]
        else:
            break

    # 내 기준 오른쪽
    # 내 기준 왼쪽
    light_dir = grid[idx][2]
    rd = -d
    for i in range(idx + 1, 4):
        if grid[i][6] != light_dir:
            rotate_arr[i] = True
            dir_arr[i] = rd
            rd *= -1
            light_dir = grid[i][2]
        else:
            break

def rotation():
    for i in range(4):
        if rotate_arr[i]:
            dirs = dir_arr[i]
            grid[i].rotate(dirs)

for order in range(order_num):
    idx, d = map(int, input().split())
    idx -= 1

    rotate_arr = [False] * 4
    dir_arr = [0] * 4
    rotate_arr[idx] = True
    dir_arr[idx] = d

    is_rotation()
    rotation()

ans = 0
for i in range(4):
    if grid[i][0]:
        ans += 2 ** i
print(ans)

