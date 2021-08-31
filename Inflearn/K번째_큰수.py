import sys
sys.stdin=open("3. k번째 큰 수/in1.txt",'rt')
N, K= map(int, input().split())
Num=list(map(int, input().split()))
ans=set()
for i in range(N):
  for j in range(i+1,N):
    for h in range(j+1,N):
      ans.add(Num[i]+Num[j]+Num[h])

ans=list(ans)
ans.sort(reverse=True)
print(ans[K-1])