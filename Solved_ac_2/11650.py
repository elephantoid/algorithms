import sys
n= int(sys.stdin.readline())
a=[]
for i in range(n):
    x, y =  map(int, sys.stdin.readline().split())
    a.append((x, y))
a = sorted(a, key = lambda x : (x[0], x[1]))

for x, y in a:
  print(x, y)

# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
