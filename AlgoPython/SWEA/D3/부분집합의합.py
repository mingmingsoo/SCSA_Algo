T = int(input())
for tc in range(T):
    arr = list(range(1, 13))
    n = 12
    m, k = map(int, input().split())
    # n개를 뽑아서 합한게 k인 애들이 몇개인지..
    # 조합으로 풀어보겠습니다.

    sel = [0] * m
    ans = 0


    def combi(idx,sidx):
        global ans
        if(sidx ==m):
            if(sum(sel)==k): # 조건 검사.
                ans+=1
            return
        if(idx ==n):
            return

        sel[sidx] = arr[idx] # 선택하고
        combi(idx+1,sidx+1)  # 다음인덱스로 넘어가.
        combi(idx+1,sidx) # 그 다음 인덱스도 idx 넘겨줄거야



    combi(0,0)
    print(f"#{tc+1} {ans}")