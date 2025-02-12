n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse= True) # 큰 숫자들부터 차례차례 확인한다
ans = 0
for coin in arr:
    if(coin<=k): # 만약 돈이 목표 금액보다 작으면 계산 가능
       ans += (k//coin) # 몫 만큼 더하고
       k = k -  (k //coin)*coin # 내가 가진 돈은 그만큼 빼준다
    if(k==0):
        break
print(ans)