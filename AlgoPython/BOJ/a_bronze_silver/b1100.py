'''
하얀칸 위에 말이 몇개 있는가?
'''

grid = [list(input()) for i in range(8)]
ans = 0

for i in range(8):
    for j in range(8):
        if (i+j)%2 ==0 and grid[i][j]=="F":
            ans+=1

print(ans)