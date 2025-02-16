'''
[문제설명]
    1에 위치한 하노이탑을 3으로 모두 이동시키는 데
    최소 이동 횟수는?
'''

n = int(input()) # 탑의 높이
arr = [[] for i in range(3)]
end = [[] for i in range(3)]
noEnd = [[] for i in range(3)]
for i in range(1,n+1):
    arr[0].append(i)
    end[2].append(i)
    noEnd[1].append(i)
print(arr)
def hanoi(f,t,path):
    if(arr == noEnd):
        return
    if(arr == end):
        print(path)
        return
    for i in range(3):
        for j in range(3):
            if(t==i):
                continue
            if(t==i and f==j):
                continue
            if(i==j):
                continue
            if(not arr[i]):
                continue
            if(not arr[j] or arr[i][0] < arr[j][0]):
                arr[j].insert(0,arr[i].pop(0))
                path.append((i+1,j+1))
                hanoi(i,j,path)
                arr[i].insert(0, arr[j].pop(0))
                path.pop()

hanoi(0,-1,[]) # from, to, list
