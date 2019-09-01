# coding=utf-8

line1 = input().split(' ')
row = int(line1[0])
k = int(line1[1])
column = []
for i in range(row):
    s = input().split(' ')
    column.append(s)


def get_value(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


for i in range(row):
    result = 0
    left = int(column[i][0])
    right = int(column[i][1])
    for j in range(left, right + 1):
        if j < k:
            result += 1
        elif j == k:
            result += 2
        else:
            time = j // k
            for l in range(1, time + 1):
                first = get_value(j - (k - 1) * l)
                second = get_value(l)
                third = get_value(j - (k - 1) * l - l)
                ans = first / (second * third)
                result += ans
            result += 1

    print(int(result))
