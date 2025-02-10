n = int(input())
card = list(map(int, input().split()))
arr = [1]


for i in range(1,n):
    # i는 원래 append 돼야하는데
    # 만약 card가 0이 아니면 그 앞 인덱스로감
    if(card[i]==0):
        arr.append(i+1)
    else:
        # print(len(arr)-card[i])
        arr.insert(len(arr)-card[i],i+1)
print(*arr)



