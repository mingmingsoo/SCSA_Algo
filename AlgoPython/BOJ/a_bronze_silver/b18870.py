n =int(input())
inputList = list(map(int, input().split()))
# 순위를 매기고 싶은데... 방법이 잘...

sortedList = sorted(list(set(inputList)))
# print(sortedList)
# print(list(range(len(sortedList))))

idxList = list(range(len(sortedList)))

dictList = dict(zip(sortedList, idxList))
# print(dictList)

for x in inputList:
    print(dictList[x], end = " ")

