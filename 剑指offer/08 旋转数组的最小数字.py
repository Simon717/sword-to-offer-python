# -*- coding: utf-8 -*-
"""
   File Name：     08 旋转数组的最小数字
   Description :
   Author :       YYJ
   date：          2019-02-13
"""
# -*- coding:utf-8 -*-


class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        """
        :type rotateArray: List[int]
        :rtype: int
        """
        l, r = 0, len(rotateArray) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if rotateArray[mid] < rotateArray[mid - 1]: # 边界条件 对于数组只有一个数字的情况 mid - 1 = - 1 == [0]
                return rotateArray[mid]

            elif rotateArray[mid] < rotateArray[l]:
                r = mid - 1
            elif rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            else:
                return rotateArray[l]


if __name__ == '__main__':
    testArr = [1]
    solu = Solution()
    print(solu.minNumberInRotateArray(testArr))
