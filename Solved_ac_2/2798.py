import sys
from itertools import combinations

n, m =map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))

best_=list(combinations(cards, 3))
new_best=[]
 
for i in range(len(best_)):
    new_best.append(sum(best_[i]))

result=[]
for i in range(len(new_best)):
    if new_best[i] <= m:
        result.append(new_best[i])

print(sorted(result, reverse=True)[0])

'''
1. card의 모든 조합 구함
조합은 하나 하나 튜플의 형태로 저장됨
2. 각 조합의 sum을 리스트에 저장
3. set()을 이용해 중복 제거
4. m과 비교하기
5. sorted reverse를 이용해 가장 큰 값이 result[0]에 위치
'''
