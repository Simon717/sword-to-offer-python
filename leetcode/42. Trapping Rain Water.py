# -*- coding: utf-8 -*-
"""
   File Name：     42. Trapping Rain Water
   Description :
   Author :       simon
   date：          19-4-15
"""
import copy

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         minus = 0
#         res = 0
#
#         nums = copy.deepcopy(height)
#         # max1 = max(nums)
#         # idx1 = nums.index(max1)
#         # nums[max1] = 0
#         # max2 = max(nums)
#         # idx2 = nums.index(max2)
#         # nums[max2] = 0
#         index = sorted(range(len(nums)), key=lambda k: nums[k])
#         index = index[::-1]
#         left, right = min(index[:2]), max(index[:2])
#         while index:
#             res += (right - left - 1) * min(nums[left], nums[right])
#             res -= sum(nums[left+1:right])
#             del
#

"""
需要使用积分的思路做
去观察什么样的数字可以拿到雨水 大概的想法就是左边高 右边也高 中间低 这个中间的元素就能够接到雨水
所以需要知道当前元素的左边有没有更大的元素 当前元素的右边有没有更大的元素 有的话就能接到水
当我位于i位置的时候 我需要知道此时左边的最大值和右边的最大值
leftmax[i]
rightmax[i]
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        l = r = res = 0

        for i in range(len(height)):
            leftmax[i] = l = max(height[i], l)

        for i in range(len(height) - 1, -1, -1):
            rightmax[i] = r = max(r, height[i])

        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res


# class Solution_stack(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         stack = [0]
#         res = 0
#         for i in range(1, len(height)):
#             if height[i] > height[stack[-1]]:
#                 res += (i - stack[-1]) * height[stack[-1]] - sum(height[stack[-1]:i])
#                 stack.pop()
#                 stack.append(i)
#         #
#         # print(res)
#
#
#         if stack[-1] != len(height)-1:
#             rightmax = 0
#             rightidx = stack[-1] + 1
#             for i in range(stack[-1] + 1, len(height)):
#                 if height[i] >= rightmax:
#                     rightmax = height[i]
#                     rightidx = i
#             res += (rightidx - stack[-1]) * height[rightidx] - sum(height[stack[-1] + 1:rightidx + 1])
#         return res

"""
堆栈解往往是 一个一个压入 连续地弹出

当前元素小于等于栈顶的元素 将其压入堆栈 因为当前元素可以被栈内的前一个元素兜住
如果当前元素大于了栈顶的元素 那么栈顶的元素可以被左边和右边的元素兜住 我们就可以计算兜住的雨水

We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack,
 which means that the current bar is bounded by the previous bar in the stack. 
If we found a bar longer than that at the top, we are sure that the bar at the top of 
the stack is bounded by the current bar and a previous bar in the stack
"""
class Solution_stack_:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]: # 当前元素比栈内最后一个元素大
                mid = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[mid]
                res += distance * bounded_height
            stack.append(i)
        return res



if __name__ == '__main__':
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(nums))
    print(Solution_stack_().trap(nums))
