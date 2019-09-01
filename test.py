# coding=utf-8
import sys
import heapq

for line in sys.stdin:
    a = line.split(" ")
    num = [int(x) for x in a]

    n = num[0]
    m = num[1]
    k = num[2]
    print(n, m, k)
    array = []
    output = []
    i = n
    j = m


    def search(i, j, k, output):
        while i >= 0 and j >= 0:
            if len(output) == k:
                array.append(output[-1])
                output.pop(-1)
            if len(output) < k:
                output.append(i * j)
                left = search(i - 1, j, k, output)
                right = search(i, j - 1, k, output)
        return


    search(i, j, k, output)
    print(max(array))
