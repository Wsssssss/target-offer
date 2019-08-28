# 题目描述
# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？


class Solution:
    def ReverseSentence(self, s):
        if s == None or len(s) <= 0:
            return ''

        strlist = list(s)
        strlist = self.Reverse(strlist)
        begin = 0
        end = 0
        newlist = []
        result = ''
        while end < len(s):
            if end == len(s) - 1:
                newlist.append(self.Reverse(strlist[begin:]))
                break
            if strlist[begin] == ' ':
                begin += 1
                end += 1
                newlist.append(' ')
            elif strlist[end] == ' ':
                newlist.append(self.Reverse(strlist[begin:end]))
                begin = end
            else:
                end += 1

        for i in newlist:
            result += ''.join(i)
        return result

    def Reverse(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
