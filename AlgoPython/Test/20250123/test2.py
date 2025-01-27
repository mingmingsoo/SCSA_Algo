arr = []
for i in range(10):
    arr.append(int(input()))

ans = float('inf')
sum = 0
sol = 0
for i in range(10):
    sum += arr[i]
    diff = abs(sum - 100)
    if(diff <= ans):
        ans = diff
        sol = sum
print(sol)

