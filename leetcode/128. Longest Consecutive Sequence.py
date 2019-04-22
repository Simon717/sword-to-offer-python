# -*- coding: utf-8 -*-
"""
   File Name：     128. Longest Consecutive Sequence
   Description :
   Author :       simon
   date：          19-4-16
"""

"""
要求复杂度 O(n)
如果先排序 然后使用maxend 也可以解决 O(nlgn)
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        res = 1
        maxend = [nums[0]]
        for n in nums[1:]:
            if n - maxend[-1] == 1:
                maxend.append(n)
            else:
                maxend = [n]

            res = max(res, len(maxend))
        return res


"""
这道题数字的顺序无所谓 因此可以考虑hash表
使用hash表 对于每一个见过的数字 hash表的value存放包含这个数字的最长的序列的长度
"""


class Solution_hash(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = {}
        res = 0
        for n in nums:
            if n not in maxlen: # 只关心没有见过的数字 如果数字已经出现 直接跳过
                left = maxlen.get(n - 1, 0)
                right = maxlen.get(n + 1, 0)
                curlen = left + right + 1
                res = max(res, curlen)
                maxlen[n] = curlen
                maxlen[n - left] = curlen # 只需要维护边界的最大长度 中间的数字之后不会区访问了
                maxlen[n + right] = curlen
        return res


if __name__ == '__main__':
    test = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(Solution().longestConsecutive(test))
    print(Solution_hash().longestConsecutive(test))
