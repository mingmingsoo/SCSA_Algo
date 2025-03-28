'''
색깔 다 바꾸면 2^만승..;
최대 연속된 애를 찾아서 바꿔야할 듯..
start, end 를 기록

아후 왤케 생각하기 싫어
생각해 생각해 머리써 머리써

'''

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.append(0)
while True:
    bomb = False
    for i in range(len(arr)):
        diff = 0
        same = 1
        next_idx = i
        same_bomb = False
        for j in range(i + 1, len(arr)):
            if arr[i] != arr[j]:
                diff += 1
            else:
                same += 1
            if diff >= 2:
                next_idx = j
                break
            if same >=4 and diff == 0:
                next_idx = j
                same_bomb = True
                break

        if next_idx - i >= 4:
            # 터쳐...
            bomb = True
            for j in range(next_idx, i - 1, -1):
                arr.pop(j)
        if same_bomb:
            bomb = True
            for j in range(next_idx, i - 1, -1):
                arr.pop(j)
        if bomb:
            break
    if not bomb:
        break
print(len(arr))
