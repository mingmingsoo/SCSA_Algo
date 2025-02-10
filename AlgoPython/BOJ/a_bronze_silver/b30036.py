'''
고민되는 것: 잉크 색을 결정해주는 리스트가 부족하진 않은가??
-> 잉크 없는데 쏘면 잉크 색 안넘어가는 줄 알았는데,
테케보고 넘어가는거 확인해서 모듈러스로 처리했음!
'''
def first():
    global r,c
    for i in range(N):
        for j in range(N):
            if (grid[i][j] == "@"):
                r, c = i, j
                grid[i][j] = "."
                return # 이거 쓰려고 함수 만들었다.


def shot(r, c, power, color): # 잉크 쏘는 함수.
    for i in range(N):
        for j in range(N):
            if(abs(i-r)+abs(j-c)<=power and grid[i][j]!="."): # 처음에 # 으로 해서 이미 덮인 애들이 색깔 변경이 안됐음 ㅠㅠ
                grid[i][j]= color

def game():
    global power, color_idx, r, c
    for order in order_list:
        if (order in "UDLR"):
            d = "UDLR".index(order)
            nr = r + row[d]
            nc = c + col[d]
            if (not (0 <= nr < N and 0 <= nc < N)):
                continue
            if (grid[nr][nc] == "."):
                r = nr
                c = nc
        elif (order == "j"):
            power += 1
        elif (order == "J"):
            if (power <= 0):
                color_idx = (color_idx + 1) % I
                continue  # 못쏘면 넘어가
            color = color_list[color_idx]

            shot(r, c, power, color)
            power = 0
            color_idx = (color_idx + 1) % I

# 초기값 설정
I, N, orderNum = map(int, input().split()) # 컬러리스트, 맵 크기, 주문횟수
color_list = list(input())
grid = [list(input()) for i in range(N)]
order_list = list(input())
r, c, d = -1,-1,-1
power = 0
row = [-1,1,0,0]
col = [0,0,-1,1]
color_idx = 0

# 처음 위치 설정
first()
# 게임 시작
game()
# 플레이어 위치 반영해주기
grid[r][c]="@"

for _ in grid:
    print("".join(_))



