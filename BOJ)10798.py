a = [[0] * 15 for i in range(5)]
for i in range(5):
    s = list(input())
    s_len = len(s)
    for j in range(s_len):
        a[i][j] = s[j]
for i in range(15):
    for j in range(5):
        if a[j][i] == 0:
            continue;
        else:
            print(a[j][i], end='')