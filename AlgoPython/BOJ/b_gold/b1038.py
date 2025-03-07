'''
감소하는 수의 최댓값은 9876543210 총 10자 ! 임
조합을 만들어서 얘네의 인덱스를 추적한다.
'''
n = int(input())
if n >= 1023:
    print(-1)
else:
    ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    def combi(sidx, idx):
        if sidx == i:
            sel_copy = sel[:]
            sel_copy.sort(reverse=True)
            ans.append(int("".join(map(str, sel_copy))))
            return
        if idx == 10:
            return
        sel[sidx] = arr[idx]
        combi(sidx + 1, idx + 1)
        combi(sidx, idx + 1)


    for i in range(2, 11):  # 뽑을 갯수
        # 조합으로 뽑고 reverse True
        sel = [0] * i
        combi(0, 0)
    ans.sort()
    print(ans[n])
