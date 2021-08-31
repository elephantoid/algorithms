############Sol-1########
import sys
sys.stdin=open("1. k번째 약수/in3.txt", 'rt')
n, k= map(int, input().split())

cnt=0
for i in range(1,n+1):
  if n%i==0:
    cnt+=1
  if cnt==k:
    print(i)
    break
else:
  print(-1)


###########Sol-2############

N, K= map(int, input().split())
divisor=[]
for i in range(1,N+1):
  if N%i==0:
    divisor.append(i)
  
if len(divisor)<K:
  print(-1)
else:
  print(divisor[K-1])