while int(s:=input()):print(['no','yes'][s==s[::-1]])
# print(['거짓일경우','참일경우'] [조건])

#----- mine
while True:
    a=input()
    if a=='0':
        break
    answer='no'
    if a==a[::-1]:
        answer='yes'
    print(answer)