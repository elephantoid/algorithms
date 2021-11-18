n = int(input())
arr = list(map(int, input().split()))
cnt=0
for num in arr:
    error=0
    if num > 1: # 1보다 큰 수 중에
        for i in range(2,num): # 2부터 나눠보기
            if num%i==0: # 1이 아닌 수로 나뉘어지면 소수가 아님
                error+=1 # 그래서 error +=1
        if error==0: # 2부터 나누어 봤을 때 error가 0이면 1이 최대공약수
            cnt+=1
print(cnt)