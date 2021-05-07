# 1번째 BFS
N = int(input())                    # 사람 수 
A, B  = map(int, input().split())   # 타겟 
edge  = int(input())                # 관계 수
graph = [[]for i in range(N+1)]     # 관계를 저장하기 위한 그래프
visit_list= [0]*(N+1)               # Start -> End로 걸리는 거리를 기록
 
for i in range(edge):      # 그래프 저장
    P, C = map(int, input().split())
    graph[P].append(C)#양방향으로 Edge를 추가
    graph[C].append(P)
 
 
 
def bfs(start, end):    # 시작부터 끝까지 탐색
    queue = [start]
    visited = []
    
    while queue:
        V= queue.pop(0)
        visited.append(V)
        if V==end:
            break
 
        for c in graph[V]:
            if c not in visited:
                visit_list[c] = visit_list[V] + 1#현재방문 번째 수=전에 방문했던 번째수 + 1  
                queue.append(c)# queue에 graph[v]의 원소를 삽입
 
 
    if visit_list[end]==0:
        print(-1)
    else:
        print(visit_list[end])  ]

 
bfs(A,B)