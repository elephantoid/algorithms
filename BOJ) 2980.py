import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pos = 0 # 현재 위치
answer = 0 #경과 시간

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    # 신호등이 빨간불일 경우
    if answer % (r+g) <= r:
        answer += (r - (answer%(r+g)))
#마지막 신호등에서 끝사이의 거리+
answer += (L-pos) 
print(answer)