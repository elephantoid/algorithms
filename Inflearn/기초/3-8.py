n=int(input())
#a=[list(map(int, input().split())) for _ in range(n)]
a=[
  [10, 13, 10, 12, 15],
[12, 39, 30, 23, 11],
[11, 25, 50, 53, 15],
[19, 27, 29, 37, 27],
[19, 13, 30, 13 ,19]
]
t=int(input())
for i in range(t):
  x,y,z= map(int, input().split())
  if y==0:
    new_r=a[x-1]
    q=[]
    for j in range(z):
      q.append(new_r[0])
      new_r.pop(0)
    new_r= new_r+q
    a[x-1]=new_r
    print(a[x-1])
  else:
    new_r=a[x-1]
    q=[]
    for j in range(z):
      q.append(new_r[-1])
      new_r.pop()
    q=q[::-1]
    new_r=q+new_r
    a[x-1]=new_r
    print(a[x-1])
cnt=0
s, e=0, n-1
for i in range(n):
  for j in range(s, e+1):
    cnt+=a[i][j]
  if i < n//2:
    s+=1
    e-=1
  else:
    s-=1
    e+=1 

print(cnt)