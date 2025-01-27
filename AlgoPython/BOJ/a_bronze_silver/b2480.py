a, b, c = map(int, input().split())
score = 0
if(a==b==c):
    score = 10000+a*1000
elif(a==b or b==c or a==c):
    if(a==b):
        score = 1000+a*100
    elif(b==c):
        score = 1000 + b * 100
    elif(a==c):
        score = 1000 + a * 100
else:
    max = max(a,b,c)
    score = max*100
print(score)