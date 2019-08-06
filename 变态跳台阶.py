# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        ans = []
        ans.append(0)
        ans.append(1)
        ans.append(2)
        for i in range(3, number + 1):
            sum = 1
            for j in range(0, i):
                sum += ans[j]
            ans.append(sum)
        return ans[number]
