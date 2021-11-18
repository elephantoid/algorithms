import sys
t= int(sys.stdin.readline())
for i in range(t):
  H, W, N=map(int, sys.stdin.readline().split())

  if N%H==0: # h의 배수라면 0이 되버리기 때문에 예방
    a=H
    b=N//H
  else:
    a= N%H
    b= (N//H)+1
  print(f'{a*100+b}')