from collections import deque
def bfs():
  q= deque()
  q.append(N)

  while q:
    V= q.popleft()
    if V==K:
      print(time[V])
      return
    for step in (V-1, V+1, V*2):
      if 0 <= step < Max and not time[step]:
        time[step] = time[V]+1
        q.append(step)
Max = 100001
N, K= map(int,input().split())
time = [0]*Max
bfs()