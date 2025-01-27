'''
m 부터 배열의 최대값까지
이분탐색면서 나머지의 합이 m이 되는...

틀린 이유:
획득해야 되는 나무 높이가 arr 최댓값보다 클 수 있음.
그래서 시작점을 m인 나무높이로 설정하며면 안됐음..
0으로 시작해야됨.

'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))


start = 0
end = max(arr)
mid = (start+end)//2
ans = 0

def calSum(arr, mid):
    num = 0
    for i in arr:
        if(i>mid):
            num+=(i-mid)
    return num

# 2 1
# 2 2 답 1
while(start<=mid):
    sum = calSum(arr, mid)
    # print(start, mid, end, sum)
    if(sum>=m):
        ans = mid
        start = mid+1
        mid = (start+end)//2
    elif(sum <m):
        end = mid-1
        mid = (start+end)//2
print(int(ans))