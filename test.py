# coding=utf-8
length = input()
length = int(length)
ar = input().split(' ')
arr = [int(x) for x in ar]


if arr == None or length <= 0:
    print('')

strnum = [str(x) for x in arr]

for i in range(len(strnum) - 1):
    for j in range(i + 1, len(strnum)):
        if strnum[i] + strnum[j] < strnum[j] + strnum[i]:
            strnum[i], strnum[j] = strnum[j], strnum[i]

print (''.join(strnum))