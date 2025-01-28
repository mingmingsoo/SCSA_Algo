n1, m1 = map(int, input().split())
map1 = [list(map(int, input().split())) for i in range(n1)]
n2, m2 = map(int, input().split())
map2 = [list(map(int, input().split())) for i in range(n2)]

ansmap = [[0]* m2 for i in range(n1)]

for i in range(n1):
    for j in range(m2):
        # print("-------------",i,j,"-------------")
        for k in range(m1):
            ansmap[i][j] += map1[i][k] * map2[k][j]
for row in ansmap:
    print(*row)