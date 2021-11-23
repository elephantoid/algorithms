import sys
queue=[]


n= int(sys.stdin.readline())
for i in range(n):
  comand = sys.stdin.readline().split()
  if comand[0]=='push':
    queue.append(comand[1])
  elif comand[0] =='top':
    if len(queue)==0:
      print(-1)
    else:
      print(queue[-1])
  elif comand[0] =='pop':
    if len(queue)==0:
      print(-1)
    else:
      print(queue.pop(-1))
  elif comand[0] =='size':
    print(len(queue))
  else:
    if len(queue)==0:
      print(1)
    else:
      print(0)