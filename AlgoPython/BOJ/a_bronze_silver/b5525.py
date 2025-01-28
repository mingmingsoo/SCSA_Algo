n = int(input()) # 2*n+1 개의 IOI가 나와야함
m = int(input())
line = input()
cnt = 0
i = 0
while(i<m):
    start = i
    end = i
    if(line[i]=='I'):
        for j in range(i+1, m):
            if((i-j)%2==0 and line[j]=='O'):
                break
            if((i-j)%2==1 and line[j]=='I'):
                break
            end = j
            if(line[end]=='O'):
                end = j-1
    if(end-start+1 >2*n):
        cnt += (end-start+1)//2-(n-1)
    i = end+1
print(cnt)