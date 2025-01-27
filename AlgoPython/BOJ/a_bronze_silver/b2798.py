n, limit = map(int, input().split())
arr = list(map(int, input().split()))

diff = float('inf')
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = arr[i]+arr[j]+arr[k];
            print(sum)
            if(abs(limit-sum)<diff and sum <= limit):
                diff = (abs(limit-sum))
print(limit-diff)
