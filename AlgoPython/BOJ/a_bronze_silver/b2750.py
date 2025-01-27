T = int(input())
list = []
for t in range(T):
    list.append(int(input()))

for i in range(T):
    for j in range(i+1,T):
        if(list[i]>list[j]):
            list[i], list[j] = list[j], list[i]
print("\n".join(map(str, list)))