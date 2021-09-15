# 다이아몬드
N=5
#a=[list(map(int, input().split)) for _ in range(N)]
a=[
  [10, 13, 10, 12, 15],
[12, 39, 30, 23, 11],
[11, 25, 50, 53, 15],
[19, 27, 29, 37, 27],
[19, 13, 30, 13, 19]
]
# center=int(N/2+0.5 -1)
# print(center)
# cnt=0
# i=0
# while i<N:
#   if i==0:
#     cnt+= a[0][center]
#     i+=1
#     continue;
#   if i==1:
#     cnt+= a[1][center]
#     cnt+= a[1][center+1]
#     cnt+= a[1][center-1]
#     i+=1
#     continue;
#   cnt+=a[i][center]
#   for j in range(1,i):
#     cnt+=a[i][center+j]
#     cnt+=a[i][center-j]
#   i+=1
# print(cnt)

#------------------------------
#------------------------------
#------------------------------
cnt=0
s=e=N//2
for i in range(N):
  for j in range(s, e+1):
    print(j)
    cnt+=a[i][j]
  if i < N//2:
    s-=1
    e+=1
  else:  
    s+=1
    e-=1
