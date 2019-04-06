# -*- coding: utf-8 -*-
"""
   File Name：     滑动窗口的最大值
   Description :
   Author :       simon
   date：          19-3-20
"""

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        curWinMax = []
        if len(num) >= size:
            index = [] # index[0] 当前最大值 index[-1]当前值 中间存放的是介于最大值和当前值之间的数值 小于当前的值的全部丢掉
                       # 队列里的元素由高到底排列 当前元素是最小的一个
            for i in range(size):
                while len(index) > 0 and num[i] > num[index[-1]]: # 清除队里比我差的选手
                    index.pop()
                index.append(i)

            for i in range(size, len(num)):
                curWinMax.append(num[index[0]]) # 添加当前队里的最大值
                while len(index) > 0 and num[i] >= num[index[-1]]: # 清除队里对我差的选手
                    index.pop()
                if len(index) > 0 and index[0] <= i - size: # 队列中的最大值超出窗口长度 已经失效
                    index.pop(0)
                index.append(i)

            curWinMax.append(num[index[0]])
        return curWinMax


# -*- coding:utf-8 -*-
class Solution_:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return []
        if len(num) < size or size < 1:
            return []

        res, candiIndex = [], []
        for i in range(size):
            while len(candiIndex) and num[i] > num[candiIndex[-1]]:
                candiIndex.pop()
            candiIndex.append(i)

        for i in range(size, len(num)):
            res.append(num[candiIndex[0]])
            while len(candiIndex) and num[i] >= num[candiIndex[-1]]:
                candiIndex.pop()
            candiIndex.append(i)
            if len(candiIndex) and candiIndex[0] <= i - size:
                candiIndex.pop(0)

        res.append(num[candiIndex[0]])
        return res


if __name__ == '__main__':

    test = [2, 3, 4, 2, 6, 2, 5, 1]
    s = Solution_()
    print(s.maxInWindows(test, 3))
