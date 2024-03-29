# 题目描述
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return False
        length = len(rotateArray)
        left = 0
        right = length - 1
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                return rotateArray[right]
            mid = (left + right) // 2
            if rotateArray[mid] == rotateArray[right] == rotateArray[left]:
                return min(rotateArray)
            elif rotateArray[left] <= rotateArray[mid]:
                left = mid
            elif rotateArray[right] >= rotateArray[mid]:
                right = mid
        return rotateArray[0]
