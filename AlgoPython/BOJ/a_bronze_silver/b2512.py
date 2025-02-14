'''
문제 설명
    예산액을 여러 지방에 분배하는데
    1. 다 줄 수 있으면 그대로 배정
    2. 예산이 모자라면 최대한 많이 줄 수 있는 만큼 배정한다.
구상
    1. 다 줄 수 있으면 다 주고 max 출력
    2. 그게 아니라면 이진탐색으로 최적점 출력 (최댓값)
'''
n = int(input())
arr = list(map(int, input().split()))
total = int(input())


if(sum(arr)<=total):
    print(max(arr))
else:

    # 예산이 부족하면
    ans = 0

    start = 0
    end = max(arr)

    while start <=end:
        middle = (start+end)//2
        ele_total = 0
        for fee in arr:
            if(fee<middle): # 주려는 돈보다 요청액이 작으면
                ele_total += fee # 그 요청액은 줄게
            else:
                ele_total +=middle # 그게 아니면 상한선까지만 줄게

        if(ele_total<=total): # 그 상한선이 총 예산보다 작거나 같으면
            ans = middle
            start = middle+1 # 조금씩 올려볼게
        else: # 돈을 너무 많이 편성해서
            end = middle-1 # 좀만 낮혀보자
    print(ans)