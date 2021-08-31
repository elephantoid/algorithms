import sys
sys.stdin=open("2. K번째 수/in2.txt",'rt')
T=int(input())
for t in range(T):
  n, s, e, k= map(int, input().split())
  a=list(map(int, input().split()))
  a=a[s-1:e]
  a.sort()
  print("#%d %d" %(t+1,a[k-1]))