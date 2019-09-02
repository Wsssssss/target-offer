import sys

strs = sys.stdin.readline().strip()
strlen = len(strs)
res = []
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                if a + b + c + d == strlen:
                    A = int(strs[:a])
                    B = int(strs[a:a + b])
                    C = int(strs[a + b:a + b + c])
                    D = int(strs[a + b + c:a + b + c + d])
                    if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                        ans = str(A) + '.' + str(B) + '.' + str(C) + '.' + str(D)
                        if len(ans) == strlen + 3:
                            res.append(ans)

result = ','.join(res)
print(result)
