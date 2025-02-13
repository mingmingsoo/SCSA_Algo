'''
[문제 설명]
    차들이 다리를 건널 수 있는 총 시간은?
[구상]
    다리들을 q로 관리해주면서
    무게가 괜찮으면 계속 넣어주고
    그렇지 않으면 0을 넣어서 대기하게한다.
'''
n, length, limit = map(int, input().split())
arr = list(map(int, input().split()))
bridge = [0]*length # 다리 상태

car_idx = 0
time = 0

while car_idx<n : # 자동차들을 순서대로 빠져나가게 할거임
    time+=1
    bridge.pop(0) # 앞에서부터 빠져나가고 뒤에서 채워줌

    if sum(bridge)+arr[car_idx]<=limit:
        bridge.append(arr[car_idx]) # 차 넣어주고
        car_idx+=1 # 다음차로 넘어가
    else:
        bridge.append(0) # 아니면 기다려
    # print(bridge)
while bridge: # 남은 애들도 빠져나오렴
    time+=1
    bridge.pop(0)
print(time)