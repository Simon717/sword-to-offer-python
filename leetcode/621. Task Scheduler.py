# -*- coding: utf-8 -*-
"""
   File Name：     621. Task Scheduler
   Description :
   Author :       simon
   date：          19-4-1
"""

import sys

"""
能通过基本的测试样例
"""

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        self.len = sys.maxsize

        def DFS(ts, path):
            if not ts:
                self.len = min(self.len, len(path))
                return

            for t in ts:
                if t not in path[-n:]:
                    ts.remove(t)
                    DFS(ts, path+[t])
                    ts.append(t)
            if ["#"]* n !=  path[-n:]: #  防止死循环
                DFS(ts, path+['#'])

        DFS(tasks, [])
        return self.len

import collections

"""
掌握这个思路就可以
两个例子足以说明问题
A??A??A
AB?AB?AB
"""
class Solution_(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks)
        part_count = max(d.values()) - 1
        mostFreqCnt = len([i for i in d.values() if i == max(d.values())]) # 最高频率任务 存在多个的情况
        empty_slots = part_count * (n - (mostFreqCnt - 1)) # 空位数目 （待填入非最高频率任务）
        available_tasks = len(tasks) - mostFreqCnt * max(d.values()) # 除去最高频率任务剩下的任务
        idles = max(0, empty_slots - available_tasks)  # 计算出空闲次数
        return len(tasks) + idles

class Solution__(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        CNT = {}
        for task in tasks:
            CNT[task] = CNT.get(task, 0) + 1
        max_freq = max(CNT.values())
        res = (max_freq-1) * (n+1)  # 总任务：AB?AB?AB  目前只计算了：AB?AB?
        for freq in CNT.values(): #　计算剩下的 AB
            if freq == max_freq:
                res += 1
        return max(len(tasks), res)

class Solution___(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = collections.Counter(tasks).values() #  各个任务的计数
        maxfreCnt = max(d) # 最高频率任务 有几个
        return max((maxfreCnt-1)*(n+1) + d.count(maxfreCnt), len(tasks))

if __name__ == '__main__':
    print(Solution().leastInterval(["A","A","A","B","B","B"], 2))