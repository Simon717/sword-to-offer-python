# -*- coding: utf-8 -*-
"""
   File Name：     08 旋转数组的最小数字
   Description :
   Author :       YYJ
   date：          2019-02-13
"""
# -*- coding:utf-8 -*-
"""
运行时间：935ms

占用内存：5624k
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return

        N = len(rotateArray)
        stt, end = 0, N-1
        if rotateArray[stt]<rotateArray[end]:
            return rotateArray[stt]
        else:
            while end-stt>1:
                mid = (stt+end)//2
                if rotateArray[mid] <= rotateArray[end]:
                    end = mid
                elif rotateArray[mid] >= rotateArray[stt]:
                    stt = mid
                elif rotateArray[mid]==rotateArray[stt]==rotateArray[end]:
                    minVal = rotateArray[stt]
                    for item in rotateArray[stt:end+1]:
                        if item < minVal:
                            minVal = item
                    return minVal

if __name__ == '__main__':
    testArr = [3,4,5,1,2]
    solu = Solution()
    print(solu.minNumberInRotateArray(testArr))