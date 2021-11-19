import sys
n = int(sys.stdin.readline())
a=[]
for _ in range(n):
  a.append(int(sys.stdin.readline()))

for i in sorted(a):
  print(i)

#####################################################
import sys
print(*sorted(list(map(int,sys.stdin.readlines()[1:]))))
'''
첫번째 N을 제외하고 그 뒤에 오는 숫자들의 개수만큼 *를 이용해 출력
하지만 1번 풀이가 더 빠름
'''