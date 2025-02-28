'''
풀이시간
    1차제출: 26분
    ~3차제출: 6분
    ~제출완료: 12분 -> 문제 다시 읽고 판화 문제 생각나서 조건 수정했음
    총 46분

문제설명
    아리가 기절하면 마!
    기절 안하면 퓨..

    아리와 좀비들은 모두 아래를 봄
    F 전진 L 회전 R 회전
    *벽에 부딪히면 전진하지 못하고 제자리에 머문다. -> 별까지 쳐놓고 여기서 틀렸습니다.
    아리가 스위치칸에 도착하면 좀비 마주치기 전에 스위치를 켬 => 이게 중요
    스위치 키면 8방으로 불 켜짐
    좀비들은 아리 움직일때마다 움직임
    만약 좀비들이 벽에 부딪히면 반대방향으로 돈다.

입력
    맵크기
    이동리스트
    맵(S: 형광등, Z: 좀비)

구상
    좀비들은 1차원으로 관리

# 틀린이유 ... 아리가 가만히 있을 떄 continue 처버림 ;ㅠㅠ
# 가만히 안있을 때만 위치 갱신하는걸로 바꾸니까 맞았다.

'''
# 불 켜주는 함수
def brighting(r, c):
    light_grid[r][c] = True
    for k in range(8):
        nr = r + row_light[k]
        nc = c + col_light[k]
        if not (0 <= nr < n and 0 <= nc < n):
            continue
        light_grid[nr][nc] = True

def moving():
    # 아리가 이동할 때마다
    # 0, 범위확인
    # 1, 스위치 있는지 확인

    r, c, d = 0, 0, 0  # 아리 위치

    for o in order_list:
        if o == "F":
            nr = r + row[d]
            nc = c + col[d]

            # ★★★★ 이거때문에 틀렸음!! 이러면 좀비이동이 안됩니다 ㅠㅠㅠ★★★★
            # if not (0 <= nr < n and 0 <= nc < n):
            #     continue

            # 그래서 갈 수 있을 때만 가는 조건으로 바꿈
            # 스위치 있으면 밝히기
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == "S":
                brighting(nr, nc)
                r = nr
                c = nc
            else: # 이동할 수 있으면 이동하기
                if(0 <= nr < n and 0 <= nc < n):
                    r = nr
                    c = nc

        # 방향전환
        elif o == "R":
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

        # 좀비랑 같은 위치인 지 확인
        for zr, zc, zd in zombie_list:
            if r == zr and c == zc and not light_grid[r][c]: # 스위치 밖이라면
                print("Aaaaaah!")
                return

        # 좀비 이동
        for i in range(len(zombie_list)):
            zr = zombie_list[i][0]
            zc = zombie_list[i][1]
            zd = zombie_list[i][2]

            nzr = zr + row[zd]
            nzc = zc + col[zd]

            if not (0 <= nzr < n and 0 <= nzc < n):
                zd = (zd + 2) % 4
            else:
                zr = nzr
                zc = nzc
            zombie_list[i][0] = zr
            zombie_list[i][1] = zc
            zombie_list[i][2] = zd


        # 다시 확인해줘야됨 -> 여기서 확인 안해주면 틀림
        # 아리가 이동하고 나서 좀비 확인해주고,
        # 좀비가 이동하고 나서 아리 위치로 갈 수 도 있어서 두번 확인해줘야된다.
        for zr, zc, zd in zombie_list:
            if r == zr and c == zc and not light_grid[r][c]: # 스위치 밖이라면
                print("Aaaaaah!")
                return


    print("Phew...") # 여기까지 왔으면 안전하다


n = int(input())
order_list = list(input())
grid = [list(input()) for i in range(n)] # 맵 -> 사실은 필요 없음
light_grid = [[False] * n for i in range(n)] # 조명

# 아리, 좀비를 위한
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

# 스위치를 위한
row_light = [1, 0, -1, 0, 1, 1, -1, -1]
col_light = [0, -1, 0, 1, 1, -1, 1, -1]

# 좀비들 1차원으로 관리
zombie_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == "Z":
            zombie_list.append([i, j, 0])  # 좀비 위치와 방향

moving()

