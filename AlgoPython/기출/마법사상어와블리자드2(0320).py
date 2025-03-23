'''
다르게 풀어보깅
'''


def make_location():  # 한번만 실행하는 함수, 달팽이 순서대로 위치 담아주기
    # 달팽이용 방향
    s_row = [0, 1, 0, -1]
    s_col = [-1, 0, 1, 0]
    r, c, d = n // 2, n // 2, 0
    num, two, cnt = 1, 0, 0
    while not (r == 0 and c == 0):

        location_idx.append((r, c))

        r = r + s_row[d]
        c = c + s_col[d]

        cnt += 1
        if cnt == num:
            d = (d + 1) % 4
            cnt = 0
            two += 1
        if two == 2:
            two = 0
            num += 1
    location_idx.pop(0)  # 가운는 빼주고
    location_idx.append((0, 0))  # 맨 끝에는 넣어주기


def attack():  # 공격!
    for dist in range(1, distance + 1):
        nr = r + row[d] * dist
        nc = c + col[d] * dist
        grid[nr][nc] = 0


def pull():  # 당겨! :
    arr = []
    for r, c in location_idx:
        if grid[r][c] != 0:
            arr.append((grid[r][c]))
    return arr


def bomb():
    global arr
    while True:
        arr.append(0)
        is_bomb = False
        no_bomb = []
        same = arr[0]
        tmp = [same]
        idx = 1
        while idx < len(arr):
            num = arr[idx]
            if num == same:
                tmp.append(num)
            else:
                if len(tmp) >= 4:
                    ans[tmp[0] - 1] += len(tmp)
                    is_bomb = True
                    tmp = [num]
                    same = num
                else:
                    no_bomb.extend(tmp)
                    same = num
                    tmp = [num]
            idx += 1
        arr = no_bomb
        if not is_bomb:
            break


def fill():
    global grid

    arr.append(0)  # 마지막 숫자 비교를 위해 0 넣어줌
    new_arr = []
    same = arr[0]  # 일단 첫번째 숫자를 스타트로
    cnt = 1
    idx = 1
    while idx < len(arr):
        num = arr[idx]
        if num == same:  # 같으면 갯수 증가
            cnt += 1
        else:
            new_arr.append(cnt)  # 아니면 여태 몇개였는지 추가
            new_arr.append(same)
            same = num
            cnt = 1  # cnt 초기화
        idx += 1

    grid = [[0] * n for i in range(n)]  # 배열 새로!
    for r, c in location_idx:  # 새로 만들어진 숫자들 넣어주기
        # 아무리 많아도 map을 채울 수 있는 만큼만
        if new_arr:
            grid[r][c] = new_arr.pop(0)


row = [-1, 1, 0, 0]  # 공격용 방향
col = [0, 0, -1, 1]
n, attack_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
location_idx = []
make_location()
r, c = n // 2, n // 2
ans = [0, 0, 0]  # 정답 출력용

for a in range(attack_num):
    d, distance = map(int, input().split())  # 공격 방향과 거리
    d -= 1

    attack()  # 공격
    arr = pull()  # 당겨줌
    bomb()  # 폭발
    fill()  # 채워줌
print(ans[0] * 1 + ans[1] * 2 + ans[2] * 3)
