
s1 = 'abcdefg'
s2 = 'cdgf'
m = [[0 for i in range(len(s2)+1)]for j in range(len(s1)+1)]

nmax = 0
p = 0

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            m[i+1][j+1] = m[i][j]+1
            if m[i+1][j+1]>nmax:
                nmax = m[i+1][j+1]
                p = i+1
print(m)
