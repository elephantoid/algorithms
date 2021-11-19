import sys
n, k=map(int, sys.stdin.readline().split())
def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)
print(bino_coef(n, k))
'''
재귀를 이용해 이항계수를 구하는 방식
n or k 가 0 이되면 1이다  
전체 집합에서 모두를 뽑는 경우와 아예 안뽑은 경우 모두 1가지이기 때문
이항계수 성질을 이용해 재귀문 반복 // 하지만 성능이 안좋음 부분반복 때문
'''

import sys
from itertools import combinations
n, k=map(int, sys.stdin.readline().split())
n_=list(i for i in range(1, n+1))
comb=list(combinations(n_, k))
print(len(comb))

'''
itertools의 combinations를 이용한 방식
n은 항상 iterable해야 하기 때문에 n개의 개수를 가진 list 생성
n_ 리스트에서 k 개를 뽑기 총 개수 len으로 구하기

위 방식이 1번보다 속도가 더 빨랐음
'''