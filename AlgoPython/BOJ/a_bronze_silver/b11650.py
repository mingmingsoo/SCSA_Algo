class Coordinate:
    def __init__(self, x,y):
        self.x = x
        self.y =y
    def __lt__(self, other):
        if(self.x ==other.x):
            return self.y < other.y
        return self.x<other.x
arr = []
N = int(input())
for n in range(N):
    x,y = map(int, input().split())
    arr.append(Coordinate(x,y))
arr.sort()
for cool in arr:
    print(cool.x, cool.y)