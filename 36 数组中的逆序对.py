# -*- coding: utf-8 -*-
"""
   File Name：     36 数组中的逆序对
   Description :
   Author :       simon
   date：          19-2-25
"""

# -*- coding:utf-8 -*-
"""
运行超时
"""
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0

        sortdata = data[:]
        sortdata.sort()
        cnt = 0
        for x in sortdata:
            cnt += data.index(x)
            data.remove(x)
        return cnt

if __name__ == '__main__':
    test = [3,1,2]
    solu = Solution()
    print(solu.InversePairs(test))