length = input()
length = int(length)
arr = input().split(',')
arr = [int(x) for x in arr]

dp = [0] * (max(arr) + 1)

for i in range(len(arr)):
    if arr[i] > 0:
        dp[arr[i]] = 1

ans = 0
for j in range(1, len(dp)):
    if dp[j] == 0:
        ans = j
print(ans)
