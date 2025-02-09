n,m,r,c,ORDER_NUM = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
order_list = list(map(lambda x: int(x)-1,input().split()))
row = [0,0,-1,1]
col = [1,-1,0,0]

dice = [0,0,0,0,0,0] # 윗면,밑면,앞면,뒷면,왼쪽면,오른쪽면
ans = []

if(grid[r][c] != 0):
    dice[1] = grid[r][c]
    grid[r][c]=0

for i in range(len(order_list)):

    d = order_list[i]
    ans.append(dice[0])
    nr = r+row[d]
    nc = c+col[d]
    if(not(0<=nr<n and 0<=nc<m)):
        ans.pop()
        continue
    if(d==0): # 동쪽이면
        new_dice = dice[4:]+dice[2:4]+[dice[1]]+[dice[0]]
        dice = new_dice[:]
        # print(dice[0])
    elif(d==1): # 서쪽이면
        new_dice = [dice[5]]+[dice[4]]+dice[2:4]+dice[:2]
        dice = new_dice[:]
    elif(d==2): # 북쪽이면
        new_dice = dice[2:4]+[dice[1]]+[dice[0]]+dice[4:]
        dice = new_dice[:]
    elif(d==3): # 남쪽이면
        new_dice = [dice[3]]+[dice[2]]+dice[:2]+dice[4:]
        dice = new_dice[:]

    if(grid[nr][nc]==0):
        grid[nr][nc] = dice[1]
    else:
        dice[1] = grid[nr][nc]
        grid[nr][nc] = 0
    r = nr
    c = nc

ans.pop(0)
ans.append(dice[0])
for i in range(len(ans)):
    print(ans[i])