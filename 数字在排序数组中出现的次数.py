# 题目描述
# 统计一个数字在排序数组中出现的次数。

class Solution:
    def GetNumberOfK(self, data, k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.firstk(data, length, k, 0, length - 1)
            last = self.lastk(data, length, k, 0, length - 1)
            if first > -1:
                number = last - first + 1

        return number

    def firstk(self, data, length, k, start, end):
        if start > end:
            return -1

        middleindex = (start + end) // 2
        middledata = data[middleindex]

        if middledata == k:
            if middleindex > 0 and data[middleindex - 1] == k:
                end = middleindex - 1
            else:
                return middleindex
        elif middledata > k:
            end = middleindex - 1
        else:
            start = middleindex + 1
        return self.firstk(data, length, k, start, end)

    def lastk(self, data, length, k, start, end):
        if start > end:
            return -1

        middleindex = (start + end) // 2
        middledata = data[middleindex]

        if middledata == k:
            if middleindex < end and data[middleindex + 1] == k:
                start = middleindex + 1
            else:
                return middleindex
        elif middledata > k:
            end = middleindex - 1
        else:
            start = middleindex + 1
        return self.lastk(data, length, k, start, end)
