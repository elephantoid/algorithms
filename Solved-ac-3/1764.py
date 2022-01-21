# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# -----------------------------------------
import sys
n,m = map(int, sys.stdin.readline().split())

a= set()
b= set()
for i in range(n):
    a.add(sys.stdin.readline()[:-1])
for j in range(m):
    b.add(sys.stdin.readline()[:-1])

answer = sorted(list(a.intersection(b)))
print(len(answer))
for i in answer:
    print(i)
#-----------------------------------------
# from collections import Collection
# a=Collection()
# b=Collection()