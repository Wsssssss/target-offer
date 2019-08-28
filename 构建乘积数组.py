# 题目描述
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。


class Solution:
    def multiply(self, A):
        if A == None or len(A) < 1:
            return
        length = len(A)
        B = [1] * length
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        for i in range(length-2,-1,-1):
            temp = temp*A[i+1]
            B[i] = temp*B[i]

        return B