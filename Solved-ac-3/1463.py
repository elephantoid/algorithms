n= 9


memo = [0] * (n+1)

for i in range(2, n+1):
    memo[i] = memo[i-1] + 1
    print("-1 : ", memo[i])

    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2] + 1)
        print("divide 2: ", memo[i])
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3] + 1)
        print("divide 3: ", memo[i])

print('---'*10)
print(memo[n])
print('---'*10)
print(memo)