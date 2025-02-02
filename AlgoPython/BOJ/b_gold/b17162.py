'''

뒤에 넣거나
뒤에 원소 제거

맨 뒤에서부터 최소 몇개의 수를 선택해야
얘네를 mod으로 나눴을 때 ,.... mod-1 이 최소 한번 이상 나타나는가?

1: num 추가
2: pop(없으면 무시)
3: 쿼리에 대한 계산

-> 만족하지 못하면 -1 출력
-> 만족하면 최소 몇개의 수?

mod 가 몇번째에 나왔는지 정보를 담는 dict 사용해서 최소값으로 갱신하고.
길이를 찾을 때는 최댓값으로 갱신해야함.
뒤에서부터 새야됨.
'''

Q, mod = map(int, input().split())
infos = dict()
arr = []
for i in range(mod):
    infos[i] = [] # 좌표를 담는 리스트
for q in range(Q):
    order = list(input().split())
    if order[0]=="1":
        num = int(order[1])
        num_mod = num%mod
        arr.append(num_mod)
        infos[num_mod].append(len(arr))
    elif order[0] == "2":
        if(arr):
            n = arr.pop()
            infos[n].pop()
    else:
        # # 나머지가 0,1,2,... mod-1 인 수열이 존재하는가?
        if(len(arr)<mod): # 검사할 갯수도 안되면 넘어가
            print(-1)
            continue
        minIdx = -1
        isOk = True
        for m in range(mod):
            if(not infos[m]): # 나머지가 여태 안나왔으면 넘어가!
                print(-1)
                isOk = False
                break
            eleMin = len(arr)-(infos[m][-1])+1 # 각각 mod중 늦게나온 애들이 최소값이 될거임 = 뒤에서 부터 세서.
            minIdx = max(eleMin, minIdx)
        if(isOk):
            print(minIdx)
