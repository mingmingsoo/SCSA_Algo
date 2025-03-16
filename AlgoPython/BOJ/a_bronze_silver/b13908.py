n, know_num = map(int, input().split())
know = []
if know_num != 0:
    know = list(map(int, input().split()))

sel = [0]*n

ans = 0
def perm(idx):
    global ans
    if idx == n:
        for k in know:
            if k not in sel:
                return
        ans+=1
        return
    for i in range(10):
        sel[idx] = i
        perm(idx+1)


perm(0)
print(ans)