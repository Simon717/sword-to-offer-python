# -*- coding: utf-8 -*-
"""
   File Name：     最大乘积
   Description :
   Author :       simon
   date：          19-4-8
"""

"""
这个是连续子序列的最大乘积
"""
# def helper(nums):
#
#     maxdp = mindp = res = nums[0]
#     for i in nums[1:]:
#         temp = maxdp
#         maxdp = max(i, maxdp*i, mindp*i)
#         mindp = max(i, i*temp, i*mindp)
#         res = max(res, maxdp)
#     return res

"""
最大数有两种可能：
max1 max2 max3 如果全是正数 或者负数只有一个 只需要这一种情况就可以
max1 min1 min2 如果有正数 负数有两个 
分类讨论...
"""
def helper(nums):

    max3 = sorted(nums[:3])
    min2 = max3[:][:2]
    for n in nums[3:]:
        if n > max3[-1]:
            max3.pop(0)
            max3.append(n)
        elif n > max3[-2]:
            max3[0] = max3[1]
            max3[1] = n
        elif n > max3[0]:
            max3[0] = n

        if n < min2[0]:
            min2.pop()
            min2.insert(0, n)
        elif n < min2[1]:
            min2[1] = n
    return max(max3[0]*max3[1]*max3[2], max3[-1]*min2[0]*min2[1])

import sys
def helper2(nums):
    max1 = max2 = max3 = -sys.maxsize
    min1 = min2 = sys.maxsize

    for n in nums:
        if n > max3:
            max1 = max2
            max2 = max3
            max3 = n
        elif n > max2:
            max1 = max2
            max2 = n
        elif n > max1:
            max1 = n

        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n
    return max(max1*max2*max3, max3*min1*min2)



if __name__ == '__main__':
    nums = input().strip().split(' ')
    nums = list(map(int, nums))
    print(helper2(nums))
