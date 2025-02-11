'''
n개의 대피소중에 m개를 선택해서 거리를 계산
1 2 3
2 3 1
모두 같은 것이기에 조합으로 푼다.

거리를 계산하려면 다 다다랐을 때 계산할 수 있음

'''
n, m = map(int,input().split()) # 점의 갯수와 대피소 갯수.
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
# print(arr)

sel = [0]*m
ans = 10000000000

def perm(sidx, idx):
    global ans
    if(sidx ==m): # 대피소를 선택한 다음에 연산을 한다.

        # 대피소로 선택되지 못한 애들 만들어주기
        not_sel = []
        for i in range(n):
            if i not in sel:
                not_sel.append(i)

        # 집에서 대피소까지 각각의 최소거리를 계산
        ele_dist = 0
        for j in range(n-m):
            dist = 1000000000
            house_num = not_sel[j] # 몇번 집인지.
            for i in range(m):
                store_num = sel[i] # 몇번 대피소인지.
                dist = min(dist, abs(arr[store_num][0] - arr[house_num][0])+abs(arr[store_num][1] - arr[house_num][1])) # 각각을 계산 해준다음
            ele_dist = max(ele_dist,dist) # 집에서 대피소까지의 최소거리를 계산한다.
        ans = min(ele_dist,ans) # 이 대피소들까지의 최소 거리를 구한다.
        return

    if(idx ==n):
        return

    # 조합으로 배열을 선택.
    sel[sidx]=idx
    perm(sidx+1,idx+1)
    perm(sidx,idx+1)

perm(0,0)
print(ans)