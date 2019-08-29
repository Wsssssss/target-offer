# 题目描述
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

class Solution:
    # 返回对应char
    def __init__(self):
        self.cdict = {}
        self.clist = []

    def FirstAppearingOnce(self):
        while len(self.clist) > 0 and self.cdict[self.clist[0]] == 2:
            self.clist.pop(0)
        if len(self.clist) == 0:
            return '#'
        else:
            return self.clist[0]

    def Insert(self, char):
        if char not in self.cdict.keys():
            self.clist.append(char)
            self.cdict[char] = 1
        else:
            self.cdict[char] = 2
