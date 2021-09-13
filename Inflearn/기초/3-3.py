#카드 뒤집기 input s:e 구간의 칸을 뒤집어야 합니다
#---------------------------
#a=[i for i in range(1,21)]
#print(a)
a=list(range(21))

# for i in range(10):
#   x, y= map(int, input().split())
#   x, y= y, x

#   test=a[x-1:y]
#   test.sort(reverse=True)
#   res=a[0:x-1]+test+a[y+1:]
#   print(res)

for _ in range(10):
  s, e= map(int, input().split())
  
  # 짝수든 홀수는 앞뒤로 바꿔야하는 횟수=(e-s+1)//2
  for i in range(abs((e-s+1)//2)):
    a[s+i], a[e-i]= a[e-i], a[s+i]
a.pop(0)
for x in a:
  print(x, end= ' ')