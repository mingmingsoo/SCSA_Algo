while(True):
    line = input()
    if(line == "."):
        break
#  and len(stack)!=0
    stack = []
    balance = False
    balance2 = True
    for str in line:
        if(str == "(" or str == "["):
            stack.append(str)
        if((str == ")" or str == "]")):
            if(len(stack)==0):
                balance2 = False
                break
            if(str == ")" and stack[len(stack)-1]=="("):
                stack.pop()
            elif(str == ")" and stack[len(stack)-1]!="("):
                balance = False;
                break
            if(str == "]" and stack[len(stack)-1]=="["):
                stack.pop()
            elif(str == "]" and stack[len(stack)-1]!="["):
                balance = False;
                break
    if(len(stack)==0):
        balance = True
    if(balance and balance2):
        print("yes")
    else:
        print("no")