index = [-1]*26

strings = list(input())

for i in range(len(strings)):
    s = strings[i]
    idx = ord(s)-97
    if(index[idx]==-1):
        index[idx] = i
print(" ".join(map(str, index)))


