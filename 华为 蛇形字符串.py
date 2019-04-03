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

        cntUP = Counter(upper)
        cntLo = Counter(lower)

        def getChar():
            for key in list(cntUP.keys()):
                if key.lower() not in cntLo:  # 有A 无a 直接删掉A
                    cntUP.pop(key)
            res = list(cntUP.keys()) # 取出大写字母
            return res

        def delete(x):
            x = ''.join(x)
            for k in x:
                cntUP[k] -= 1
                if not cntUP[k]:
                    # del cntUP[k] # 同样的效果
                    cntUP.pop(k)

            x = x.lower()
            for k in x:
                cntLo[k] -= 1
                if not cntLo[k]:
                    # del cntUP[k]
                    cntLo.pop(k)


        def maxLen(s):
            # print(s)
            res = s[0]
            maxEnd = s[0]
            for i in s[1:]:
                # dp = dp + i if ord(i) - ord(dp[-1]) == 1 else i
                if ord(i) - ord(maxEnd[-1]) == 1:
                    maxEnd += i
                else:
                    maxEnd = i
                if len(maxEnd) > len(res):
                    res = maxEnd
            return res

        res = []
        while cntUP:
            UPstr = getChar()
            if not UPstr: break

            UPstr.sort()

            # 最长连续子序列问题
            UPcontinue = maxLen(UPstr)
            res.append(''.join(['{}{}'.format(x, x.lower()) for x in UPcontinue]))

            # 减计数  删键值
            delete(UPcontinue)
        print(res)
















if __name__ == '__main__':

    # test = 'Aa'
    # test = 'OoPpBCccbAa'

    test = 'SxxxsrR*AaAaBbSsSs'
    solu1 = Solution_()
    print(solu1.snack(test))

    # print(maxLen('abcxxxxxabcdee'))

