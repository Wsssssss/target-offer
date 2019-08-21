# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return list(ss)

        charlist = list(ss)
        charlist.sort()

        str = []

        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i - 1]:
                continue
            temp = self.Permutation(''.join(charlist[:i]) + ''.join(charlist[i + 1:]))

            for j in temp:
                str.append(charlist[i] + j)

        return str
