# -*- coding: utf-8 -*-
"""
   File Name：     347. Top K Frequent Elements
   Description :
   Author :       simon
   date：          19-3-12
"""
import collections

"""
桶排序
利用到的信息 各个元素的频数 <= N
利用桶排序 可以直接得到排序结果...

主要思路是完成 数字-->计数 转换成 计数-->数字 两张表的转变

"""
class Solution:
    def topKFrequent(self, nums, k):
        bucket, res = [[] for _ in range(len(nums) + 1)], []
        for a, b in collections.Counter(nums).items():
            bucket[b].append(a)
        for l in bucket[::-1]: # 直接得到排序结果...
            if len(l): res += l # 由大到小 只要是非空桶 就加入结果list
            if len(res) >= k: return res[ : k]


class Solution0(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}  # 手写字典进行计数
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

        bucket, res = [[] for _ in range(len(nums) + 1)], []
        for n, cnt in dic.items():
            bucket[cnt].append(n)
        for l in bucket[::-1]:
            if l: res += l
            if len(res) > k: return res[:k]
        return res

"""
两张表的转换
"""
class Solution3(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z, v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)

        arr = []

        for x in range(len(nums), 0, -1):
            if x in frq:

                for i in frq[x]:
                    arr.append(i)

        return arr[:k]

if __name__ == '__main__':
    test = [1,1,1,2,2,3]
    solu = Solution3()
    print(solu.topKFrequent(test, 2))