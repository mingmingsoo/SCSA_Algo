line = input()
line = line.replace("()","@")
stk = []
total = 0
for i in range(len(line)):
    if(line[i]=='('):
        stk.append('(')
    elif(line[i]=='@'):
        total += len(stk)
    else:
        stk.pop()
        total+=1
print(total)


