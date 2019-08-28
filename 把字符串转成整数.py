# 题目描述
# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
#  数值为0或者字符串不是一个合法的数值则返回0。

class Solution:
    def StrToInt(self, s):
        flag = False
        if s == None or len(s) < 1:
            return 0
        strlist = []
        numdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in numdict.keys():
                strlist.append(numdict[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0

        if len(strlist) == 1 and strlist[0] == 0:
            flag = True
            return 0
        sum = 0
        for i in strlist:
            sum = sum * 10 + i

        if s[0] == '-':
            sum = 0 - sum
        return sum
