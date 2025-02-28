'''
풀이시간
    20분
문제설명
    선언 기준 톱니 좌, 우 회전할 수 있는지 확인
    다르면 반대로 회전
    같으면 회전하지 않음

주의사항
    초기상태를 보고 회전 판단

필요한 메서드
    check : 왼쪽, 오른쪽 움직일 수 있는지
    rotation : 회전

필요한 변수
    isrotate
    isdir
     -> 굳이 2개인 이유: isdir 하나로 합쳐도 되는데
        디버깅하기 편하고... 용도를 분리하고 싶었음
        즉 내가 한번에 테케가 나올 자신이 없었다.ㅎ
'''
#############################################################

# 선택된 톱니바퀴 기준 왼, 오 회전 여부 확인하는 메서드
def check(idx, d):

    origin_d = d # 원래 방향 기록 밑에서 쓸거임 ↓

    for i in range(idx, T - 1): # 오른쪽 확인 여부
        d *= -1
        if grid[i][2] != grid[i + 1][6]: # 회전 가능하면 회전해!
            is_rotate[i + 1] = True
            is_dir[i + 1] = d
        else:
            break # 아니면 끝.

    d = origin_d # 바로 여기서 쓸거였음 ↑
    for i in range(idx, 0, -1): # 오른쪽 확인 여부
        d *= -1
        if grid[i][6] != grid[i - 1][2]:
            is_rotate[i - 1] = True
            is_dir[i - 1] = d
        else:
            break

# 회전해주는 메서드
def rotation(idx, d): # 위치와 회전 방향

    if d == 1:
        # 시계
        last = grid[idx].pop()
        grid[idx].insert(0, last)
    else:
        # 반시계
        first = grid[idx].pop(0)
        grid[idx].append(first)

#############################################################
T = int(input())
grid = [list(map(int, input())) for i in range(T)]
order = int(input())

for o in range(order):
    num, d = map(int, input().split())
    num -= 1

    # 매 주문마다 초기화 필요
    is_rotate = [False] * T # 돌릴 수 있는지
    is_dir = [0] * T # 어떻게 회전할건지
    is_rotate[num] = True
    is_dir[num] = d

    # 회전가능한지 드가자
    check(num, d)

    for i in range(T):
        if is_rotate[i]: # 회전 가능한 애들만 회전해
            rotation(i, is_dir[i])

#############################################################
ans = 0
for t in range(T):
    if grid[t][0] == 1:
        ans += 1

print(ans)
