# 题目描述
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ""

        string = list(s)
        stringreplace = []
        for item in string:
            if item == " ":
                stringreplace.append("%")
                stringreplace.append("2")
                stringreplace.append("0")

            else:
                stringreplace.append(item)

        return ''.join(stringreplace)
