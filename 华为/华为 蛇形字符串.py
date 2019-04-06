# -*- coding: utf-8 -*-
"""
   File Name：     华为 蛇形字符串
   Description :
   Author :       simon
   date：          19-3-20
"""

"""
重写
"""
from collections import Counter

class Solution_:
    def snack(self, s):
        s = list(s)
        upper, lower = [],  []
        for i in s:
            if ord('a') <= ord(i) <= ord('z'):
                lower.append(i)
            if ord('A') <= ord(i) <= ord('Z'):
                upper.append(i)

        upper.sort()
        lower.sort()

        UP = Counter(upper)
        LOW = Counter(lower)

        def getChar():
            for key in list(UP.keys()):
                if key.lower() not in LOW:  # 有A 无a 直接删掉A
                    UP.pop(key)
            res = list(UP.keys()) # 取出大写字母
            return res

        def decrease(x):
            x = ''.join(x)
            for k in x:
                UP[k] -= 1
                if not UP[k]:
                    # del cntUP[k] # 同样的效果
                    UP.pop(k)

            x = x.lower()
            for k in x:
                LOW[k] -= 1
                if not LOW[k]:
                    # del cntUP[k]
                    LOW.pop(k)

        # 基础的DP问题
        def maxLen(s):
            # print(s)
            res = s[0]
            maxEnd = s[0]
            for i in s[1:]:
                if ord(i) - ord(maxEnd[-1]) == 1:
                    maxEnd += i
                else:
                    maxEnd = i
                if len(maxEnd) > len(res):
                    res = maxEnd
            return res

        res = []
        while UP:
            UPstr = getChar()
            if not UPstr: break

            # UPstr.sort()

            # 最长连续子序列问题
            UPcontinue = maxLen(UPstr)
            res.append(''.join(['{}{}'.format(x, x.lower()) for x in UPcontinue]))

            # 减计数  删键值
            decrease(UPcontinue)
        return res

if __name__ == '__main__':

    # test = 'Aa'
    # test = 'OoPpBCccbAa'

    test = 'SxxxsrR*AaAaBbSsSs'
    solu1 = Solution_()
    print(solu1.snack(test))

    # print(maxLen('abcxxxxxabcdee'))

