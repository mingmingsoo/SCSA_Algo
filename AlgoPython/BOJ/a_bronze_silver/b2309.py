arr = []
for i in range(9):
    arr.append(int(input()))
diff = sum(arr) - 100 # 100이 되기엔 남는 값

# 두 값의 합이 diff 가 되는 애들이 범인임.
found = False
for i in range(9):
    for j in range(i+1, 9):
        if(arr[i]+arr[j]==diff):
            # 뒤에서부터 제거해야 중복되게 제거 안됨
            del arr[j]
            del arr[i]
            found = True
            break
    if(found):
        break
arr.sort()
for ele in arr:
    print(ele)

