a=input()
b=''
for i in range(len(a)):
    if a[i].isdigit():
        b+=a[i]
print(int(b))
b=int(b)
cnt=0
for i in range(1,b+1):
  if b%i==0:
    cnt+=1
print(cnt)