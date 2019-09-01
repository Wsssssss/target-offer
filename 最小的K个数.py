# 题目描述
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

def GetLeastNumbers_Solution(self, tinput, k):
    import heapq
    if tinput == None or k <= 0 or len(tinput) <= 0 or len(tinput) < k:
        return []
    output = []
    for i in tinput:
        if len(output) < k:
            heapq.heappush(output, -i)
        else:
            heapq.heappushpop(output, -i)

    return sorted(list(map(lambda x: -x, output)))
