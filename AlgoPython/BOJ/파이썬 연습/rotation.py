# ## 시계방향으로 회전.
# n = 5
# grid = [list(range(i, i + n)) for i in range(1, n * n + 1, n)]
# for _ in range(n):
#     print(grid[_])
#
# print()
# rotationGrid2 = list(map(list, zip(*grid)))  # 같은 열로 묶어준다고 생각.
#
# for _ in range(n):
#     print(rotationGrid2[_])
# print()
# rotationGrid90 = list(map(list, zip(*grid[::-1])))
# for _ in range(n):
#     print(rotationGrid90[_])
#
# print()
# rotationGrid_90 = list(map(list, zip(*grid)))[::-1]
# for _ in range(n):
#     print(rotationGrid_90[_])
# print()
# # 예를들어 1,1에서 회전시키고싶음
# startR = 1
# startC =1
# gridCopy = [row[startC:startC+3] for row in grid[startR:startR+3]]
# for _ in range(3):
#     print(gridCopy[_])
# gridCopyRotation = list(map(list, zip(*gridCopy[::-1])))
#
# for _ in range(3):
#     print(gridCopyRotation[_])
#
# for i in range(startR, startR+3):
#     for j in range(startC, startC+3):
#         grid[i][j] = gridCopyRotation[i-startR][j-startC]
# print()
# for _ in range(5):
#     print(grid[_])


######### 메서드 만들어보기

startR, startC, size = 1,1,3
n = 5
grid = [list(range(i,i+5)) for i in range(1,n*n+1,n)]

for _ in range(n):
    print(grid[_])
print()
def rotation(grid, startR, startC, size):
    gridCopy = [row[startC: startC+size] for row in grid[startR:startR+size]]
    # gridCopy = list(map(list,zip(*gridCopy[::-1])))
    gridCopy = list(map(list, zip(*gridCopy)))[::-1]
    for i in range(startR, startR+size):
        for j in range(startC, startC+size):
            grid[i][j] = gridCopy[i-startR][j-startC]

rotation(grid, startR, startC, size)


for _ in range(n):
    print(grid[_])