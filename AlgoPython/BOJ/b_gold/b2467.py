'''
산성 용액의 특성값은 1부터 1,000,000,000
알칼리성 용액의 특성값은 -1부터 -1,000,000,000

수열이 주어졌으 때 두개의 서로 다른 용액을 혼합하여 0에 가까운 용액을 만드는
두 용액을  출력

N은 2 이상 100,000..
이중포문 사용 불가.

투포인터는 모르겠고 이분탐색으로 풀게요


'''

n = int(input())
arr = list(map(int, input().split()))

ans =  2000000001
i, j = -1, -1

start = 0
end = n-1

while start<end:
    eleSum = arr[start]+arr[end]
    if(eleSum ==0): # 더 탐색할 필요 없음
        i = start
        j = end
        break

    if(ans> abs(eleSum)):
        ans = abs(eleSum)
        i = start
        j = end


    if(abs(eleSum)>0 and eleSum >0):
        end -= 1
    elif(abs(eleSum)>0 and eleSum <0):
        start +=1
print(arr[i],arr[j])