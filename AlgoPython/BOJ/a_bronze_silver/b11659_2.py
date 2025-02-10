import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]*n
sum_arr[0] = arr[0]
for i in range(1,n):
    sum_arr[i]= arr[i]+sum_arr[i-1]
sum_arr.insert(0,0)
# print(sum_arr)
ans = []
for i in range(m):
    s, e = map(lambda x:int(x)-1, input().split())
    ans.append(sum_arr[e+1] - sum_arr[s])
for x in ans:
    print(x)