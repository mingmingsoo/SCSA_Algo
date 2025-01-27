n = int(input())
cnt = 1
for i in range(1, int(n/2)+1):
    sum = i
    for j in range(i+1,int(n/2)+2):
        sum+=j
        if(sum == n):
            cnt+=1
            break
        elif(sum >n):
            break
print(cnt)