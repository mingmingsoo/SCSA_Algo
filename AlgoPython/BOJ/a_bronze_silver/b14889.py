'''
n개중 m개를 뽑는 조합
1234중 12를 뽑으면 안뽑힌 34가 나머지!
1234중 34를 뽑으면 안뽑힌 12가 나머지!
이 둘은 중복되는데..... 조합을 절반만 돌리겠음
-> 그렇게 하기 위해서 start를 들고 다니면서 절반 왔으면 return 하는 조건이 필요!
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

arr = list(range(n))
m = n//2
sel = [0]* m # 절반만 선택할 것

ans = 100001

def  btk(idx,sidx,start):
    global ans
    if(start == n//2): # 더이상은 중복이야
        return

    if(sidx ==m):
        not_sel = []
        for i in range(n):
            if(i not in sel):
                not_sel.append(i)
        # print(sel,not_sel)

        sel_score = 0
        for i in range(m):
            for j in range(i+1,m):
                sel_score += grid[sel[i]][sel[j]]
                sel_score += grid[sel[j]][sel[i]]

        not_sel_score = 0
        for i in range(m):
            for j in range(i+1,m):
                not_sel_score += grid[not_sel[i]][not_sel[j]]
                not_sel_score += grid[not_sel[j]][not_sel[i]]
        # print(sel_score,not_sel_score)
        ans = min(ans, abs(not_sel_score-sel_score))
        return
    if(idx==n):
        return

    sel[sidx] = arr[idx]
    btk(idx+1,sidx+1,start)
    btk(idx+1,sidx,start+1)


btk(0,0,0) # start
print(ans)
