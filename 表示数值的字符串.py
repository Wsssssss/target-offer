# 题目描述
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

class Solution:
    # s字符串
    def isNumeric(self, s):
        if s == None or len(s) < 1:
            return False
        slist = [w.lower() for w in s]
        if 'e' in slist:
            index = slist.index('e')
            left = slist[:index]
            right = slist[index + 1:]
            if '.'in right or len(right)==0:
                return False
            isleft = self.isdigit(left)
            isright = self.isdigit(right)
            return isleft and isright
        else:
            isdigit = self.isdigit(slist)
            return isdigit

    def isdigit(self, s):
        dotnum = 0
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(s)):
            if s[i] not in digit:
                return False
            if s[i] == '.':
                dotnum += 1
            if s[i] in '+-' and i != 0:
                return False
        if dotnum > 1:
            return False
        return True
