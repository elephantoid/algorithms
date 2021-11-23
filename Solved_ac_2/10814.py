import sys
n= int(sys.stdin.readline())
a=[]
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age=int(age)
    a.append([age, name])

a.sort(key = lambda member: (member[0])) 
# key sort member의 0번째 인자를 우선순위로 sort
print(a)
for member in a:
    print(member[0], member[1])