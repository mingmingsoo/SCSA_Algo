T = int(input())
for tc in range(T):
    '''
    한바퀴 돌때마다 값들은 절반으로 줄어듬 : 치즈//2
    한바퀴의 기준은 왼쪽으로 1칸씩 이동해서 화덕 크기만큼 이동해야 한바퀴임!
    치즈양이 0이면 pop(0) 해줌

    피자번호 담아줘야함!

    '''

    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    wait = []
    for i in range(m):
        wait.append([tmp[i], i + 1])  # 치즈 양과 idx
    q = wait[:n]
    wait = wait[n:]
    # print(wait)

    while True:
        # print(q)
        if (len(q) == 1): # 마지막 남은 피자 출력
            num = q.pop()[1]
            print(f"#{tc+1} {num}")
            break

        q[0][0] = q[0][0] // 2  # 치즈 반띵


        if (q[0][0] == 0): # 맨앞에 피자가 다 녹았으면
            q.pop(0) # 빼주고
            if (wait):  # 기다리는 애들이 있으면 넣어줌.
                q.append(wait.pop(0)) # 이걸 pop 안하고 wait[0] 해서 무한루프 돌았음
        else:
            q.append(q.pop(0))