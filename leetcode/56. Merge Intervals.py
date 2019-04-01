# -*- coding: utf-8 -*-
"""
   File Name：     56. Merge Intervals
   Description :
   Author :       simon
   date：          19-3-31
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
原地修改
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key= lambda x: x.start) # key 可以是一个函数表达式

        index = 0
        while index+1 < len(intervals):
            if intervals[index].end >= intervals[index+1].start:
                intervals[index].end = max(intervals[index+1].end, intervals[index].end)
                del intervals[index+1]
            else:
                index += 1
        return intervals

"""
新开辟空间
"""

class Solution_(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key = lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res

if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

