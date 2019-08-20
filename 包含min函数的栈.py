# 题目描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, node):
        self.stack.append(node)
        if self.minstack ==[] or node<self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)
    def pop(self):
        if self.stack ==[] or self.minstack ==[]:
            return None
        self.minstack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minstack[-1]
        # write code here