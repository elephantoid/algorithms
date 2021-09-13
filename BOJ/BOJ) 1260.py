N,M,V=map(int,input().split())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1 #양방향이기 때문에 a,b / b,a Matrix에 Edge를 1로 표시
visit_list=[0]*(N+1)

def dfs(V):
    visit_list[V]=1 #방문한 정점(Vertex)을 1로 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1): #현재 V가 방문되지 않았고 matrix에 edge가 1로 표시되어있으면
            dfs(i)# i를 V로 받아서 dfs를 수행

def bfs(V):
    queue=[V] #들려야 할 정점(Vertex) 저장
    visit_list[V]=0 #방문한 점 0으로 표시 (위에서 방문한 것을 1로 표시했기 때문에)
    while queue:
        V=queue.pop(0) #방문했기 때문에 queue에서 빼줌
        print(V, end=' ') #현재 방문한 정점을 출력
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1): #위와 동일
                queue.append(i)
                visit_list[i]=0 #while문을 돌기 위해서 i번째를 방문했다 미리 표시 

dfs(V)
print()
bfs(V)      