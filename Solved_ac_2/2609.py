import sys
a,b =map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

'''
유클리드 호제법을 이용한 풀이
'''