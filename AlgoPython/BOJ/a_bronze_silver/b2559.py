n, k = map(int, input().split())

arr = list(map(int, input().split()))
sumArr = [0]*n
# 초기 누적값 계산
for i in range(k):
    sumArr[k-1]+=arr[i]
ans = sumArr[k-1]

# 최댓값 찾기
for i in range(k,n):
    sumArr[i] =  sumArr[i-1]+arr[i]-arr[i-k]
    ans = max(ans,sumArr[i])
print(ans)