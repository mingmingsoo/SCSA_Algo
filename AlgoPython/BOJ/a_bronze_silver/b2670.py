# ans = 0
# n = int(input())
# list = []
# for n in range(n):
#     list.append(float(input()))
# print(list)
# for i in range(n):
#     mul = 1
#     for j in range(i,n):
#         mul *= list[j]
#         ans= max(ans, mul)
# print("{0:.3f}".format(round(ans,3)))

ans = 0
n = int(input())
list = []
for n in range(n):
    list.append(float(input()))
dp = [0]* n
dp[0] = list[0]
for i in range(1,n):
    dp[i] = max(list[i], list[i]*dp[i-1])
# print(dp)
print("{0:.3f}".format(round(max(dp),3)))