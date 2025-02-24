
'''
문제설명
    면 6개 담고 돌릴 수 있는 조합 확인
구상
    조합
    1.오른쪽 왼쪽
    2.뚜겅 바닥
    3. 앞면 뒷면
'''

grid=[[[0]*2 for i in range(2)] for i in range(6)]
# 면 채워~
color = list(map(int, input().split()))

idx = 0 # 면
for i in range(0,24,4):
    grid[idx][0][0] = color[i]
    grid[idx][0][1] = color[i+1]
    grid[idx][1][0] = color[i+2]
    grid[idx][1][1] = color[i+3]
    idx +=1
ans = 0
grid_copy = [[[0]*2 for i in range(2)] for i in range(6)]


# for h in range(6):
#     for i in range(2):
#         for j in range(2):
            # grid_copy[i][j]

# if(is_left(grid)):
#     if(is_same(grid)):
#         ans = 1

