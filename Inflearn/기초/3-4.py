# 오름차순 리스트 합하여 오름차순으로 정렬
n=3
a=[1,3,5]
m=5
b=[2,3,6,7,9]
# NlogN
# c=a+b
# print(sorted(c))

# N
p1=0
p2=0
c=[]
while p1<n and p2<m:
  if a[p1] <= b[p2]:
    c.append(a[p1])
    p1+=1
  else:
    c.append(b[p2])
    p2+=1
if p1 <n:
  c=c+a[p1:]
if p2<m:
  c=c+b[p2:]
print(c)