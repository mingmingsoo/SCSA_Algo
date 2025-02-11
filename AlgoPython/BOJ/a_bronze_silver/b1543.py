# line =input()
# origin= input()
# print(line.count(origin)) # 이렇게 풀어도 된다.


# 다르게 풀어보기.
line = list(input())
origin= list(input())

cnt = 0
start = 0
while start < len(line)- len(origin)+1: # start 지점을 옮겨주면서 단어를 찾아줄 거임
    cur_s = start # 어디서 시작할 건지.
    isOk = True
    for i in range(len(origin)):
        if(line[cur_s]==origin[i]): # 맞으면 다음 문자열도 확인
            cur_s+=1
            continue
        else:
            isOk = False # 다르면 탈출하고 스타트를 올겨줌
            start +=1
            break
    if(isOk):
        start += len(origin) # 맞다면 스타트 지점을 옮겨줌
        cnt+=1
print(cnt)