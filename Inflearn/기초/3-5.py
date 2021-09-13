# 빙고처럼 NxN행렬의 각 행과 열 대각선의 합중에 가장 큰 값을 리턴

#-----sol1------
# N=int(input())
# a= [list(map(int, input().split()))for i in range(N)]
# # 가로축
# b=[0]*N
# for i in range(N):
#   for j in range(N):
#     b[i]+=int(a[i][j])
# # print(b)

# # 세로축
# c=[0]*N
# for i in range(N):
#   for j in range(N):
#     c[i]+=int(a[j][i])
# # print(c)
# # print(max(max(b),max(c)))
# d=[0,0]

# # 좌우 대각선
# for i in range(N):
#   for j in range(N):
#     if i==j:
#       d[0]+=int(a[i][j])

# j=N-1
# # 우좌 대각선
# for i in range(N):
#   d[1]+=int(a[i][j])
#   j-=1
  
# print(max(max(b),max(c),max(d)))

#-----------------------
#-----------------------
#-----------------------
n=int(input())
a=[list(map(int, input().split()))for _ in range(n)]
largest=-2147000000
for i in range(n):
  #sum1 가로합 sum2 세로합
  sum1=sum2=0
  for j in range(n):
    sum1+=a[i][j]
    sum2+=a[j][i]
  if sum1 > largest:
    largest=sum1
  if sum2 > largest:
    largest=sum2
sum1=sum2=0
# 좌우 대각 합
for i in range(n):
  sum1+=a[i][i]
  sum2+=a[i][n-i-1] 
if sum1 > largest:
  largest=sum1
if sum2 > largest:
  largest=sum2

print(largest)