n = int(input())

arr = list(range(1,n+1))
sel = [0]*n

visited = [False]*n

def perm(idx):
    if(idx ==n):
        print(*sel)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sel[idx] = arr[i]
            perm(idx+1)
            visited[i] = False

perm(0)