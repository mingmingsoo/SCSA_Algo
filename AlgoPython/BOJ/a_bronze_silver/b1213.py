line = list(input())

line.sort()
# 정렬하고 하나씩 순서대로 빼서 쓰기
new = [0]*len(line)
num = 0
garbage = []
num = 0
while len(line)>1:
    if(line[0]==line[1]):
        new[num] = line.pop(0)
        new[len(new)-num-1] = line.pop(0)
        num +=1
    else:
        garbage.append(line.pop(0))

if line:
    # 남은게 있으면
    new[len(new)//2] = line.pop(0)
if garbage:
    new[len(new) // 2] = garbage.pop(0)

for x in new:
    if type(x) == int:
        print("I'm Sorry Hansoo")
        exit()
if(new == new[::-1]):
    print("".join(map(str,new)))
else:
    print("I'm Sorry Hansoo")
