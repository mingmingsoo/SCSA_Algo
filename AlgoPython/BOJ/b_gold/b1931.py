n = int(input())

time = [list(map(int, input().split()) )for i in range(n)]

time.sort(key= lambda x:(x[1], x[0]))

# for _ in range(n):
#     print(time[_])

endTime = 0
cnt = 0

for start, end in time:
    if(endTime<=start):
        print(start, end)
        endTime=end
        cnt+=1

print(cnt)
