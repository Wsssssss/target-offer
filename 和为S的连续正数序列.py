# 题目描述
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

class Solution:
    def FindContinuousSequence(self, tsum):
        output=[]
        left = 1
        right = 2
        while(right>left):
            sum = (left+right)*(right-left+1)/2
            if(sum==tsum):
                output.append(list(range(left,right+1)))
            elif sum<tsum:
                right+=1
            else:
                left+=1

        return output
