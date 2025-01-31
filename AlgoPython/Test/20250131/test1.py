string = input()
sol = 10
cur = string[0]
for i in range(1,len(string)):
    if(string[i]==cur):
        sol+=5
    else:
        sol+=10
        cur = string[i]


# stack = []
# stack.append(string[0])
# for i in range(1, len(string)):
#     # 만약 닫혀진다면 ans += 10
#     if(stack and string[i]==")" and stack[-1] == "("):
#         stack.append(string[i])
#         sol += 10
#     elif(stack and string[i]=="(" and stack[-1]=="("):
#         sol+=5
#         stack.append(string[i])
#     elif(stack and string[i]==")" and stack[-1] == ")"):
#         sol+=5
#         stack.append(string[i])
#     else:
#         sol+=10
#         stack.append(string[i])
print(sol)
