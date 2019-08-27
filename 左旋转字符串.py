# 题目描述
# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
# 于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

class Solution:
    def LeftRotateString(self, s, n):
        if s==None or len(s)<=0:
            return ''

        lists = list(s)
        self.reverse(lists)
        index = len(s)-n
        leftlist = self.reverse(lists[:index])
        rightlist = self.reverse(lists[index:])

        news = ''.join(leftlist)+''.join(rightlist)
        return news



    def reverse(self,list):
        left = 0
        right = len(list)-1

        while left<right:
            list[left],list[right]=list[right],list[left]
            left+=1
            right-=1

        return list