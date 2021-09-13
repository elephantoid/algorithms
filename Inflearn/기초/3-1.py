n=int(input())
for i in range(n):
    a=input()
    a=a.upper()
    if a==a[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
