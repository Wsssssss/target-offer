# 题目描述
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

class Solution:
    def FirstNotRepeatingChar(self, s):
        if s ==None or len(s)<=0:
            return -1

        slist = list(s)
        sdict = {}
        for i in slist:
            if i not in sdict.keys():
                sdict[i]=0
            sdict[i]+=1

        for i in slist:
            if sdict[i] == 1:
                return s.index(i)
        return -1