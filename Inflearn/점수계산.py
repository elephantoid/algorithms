# 점수계산
# 연속 정답이면 +1의 가중치
# 
n= int(input())
a=list(map(int, input().split()))
# n=30
# a=[1,0,1,1,1,0,0,1,1,0]


score=0
add=0
if a[0]==1:
  score+=1
  add+=1

for i in a[1:n]:
  if i==1:
    score+=1+add
    add+=1
  else:
    add=0
print(score)