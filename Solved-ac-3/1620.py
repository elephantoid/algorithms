import sys
n, m =map(int, sys.stdin.readline().split())

poke_dict={}
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip()
    poke_dict[i] = a
    poke_dict[a] = i

for _ in range(m):
    quest = sys.stdin.readline().rstrip()
    if quest.isdigit():
        print(poke_dict[int(quest)])
    else:
        print(poke_dict[quest])