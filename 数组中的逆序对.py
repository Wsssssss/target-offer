# 题目描述
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007

class Solution:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0

        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        i = start + length
        j = end
        copyindex = end
        count = 0

        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[copyindex] = data[i]
                i -= 1
                copyindex -= 1
                count += j - start - length
            else:
                copy[copyindex] = data[j]
                j -= 1
                copyindex -= 1

        while i >= start:
            copy[copyindex] = data[i]
            i -= 1
            copyindex -= 1

        while j >= start + length + 1:
            copy[copyindex] = data[j]
            j -= 1
            copyindex -= 1

        return left + right + count
