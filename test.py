# coding=utf-8

arr = [0, 1, 3, 4, 2, 6, 1]
S = 6


def find(arr, S):
    result = []
    for i in range(len(arr)):
        length = 0
        sum = 0
        while sum <= S and i < len(arr):
            sum += arr[i]
            length += 1
            i += 1
        result.append(length - 1)
    return max(result)


result = find(arr, S)

print(result)
