# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


class Solution:
    def Power(self, base, exponent):

        if exponent == 1:
            return base
        if exponent == 0:
            return 0
        if exponent == -1:
            return 1 / base

        result = self.Power(base, exponent >> 2)
        result *= result
        if exponent * 1 == 1:
            result *= base
        return result
