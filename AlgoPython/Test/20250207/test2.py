'''
누적합 이용해서 풀기

'''

n,m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]*(n)

first = 0
for i in range(m):
    first += arr[i] # 합이 시작될 수 있는 처음 값을 미리 구한다.
# print(first)


sum_arr[m-1] = first # 그 값을 0 이 아닌 m 에 넣어준다.
for i in range(m,n): # 누적합을 연산한다.
    sum_arr[i] = sum_arr[i-1]-arr[i-m]+arr[i]

ans = -float("inf")
# print(sum_arr)
for i in range(m-1,n): # 0이 아닌 m-1부터여야 하는 이유는. 수열이 다 음수면 arr[0] 이 가장 큰 값이 되어 그 값을 뱉어내기에
    # m-1 부터 해줘야한다.
    ans = max(ans, sum_arr[i])
print(ans)