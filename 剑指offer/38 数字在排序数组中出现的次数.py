# -*- coding: utf-8 -*-
"""
   File Name：     38 数字在排序数组中出现的次数
   Description :
   Author :       simon
   date：          19-2-27
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        res = 0
        length = len(data)
        stt = self.getFirst(data, k, 0, length-1)
        end = self.getLast(data, k, 0, length-1)
        if stt > -1:
            res = end - stt + 1
        return res

    # def GetFirstK(self, data, k):
    #     mid = len(data) // 2
    #     print(mid)
    #     if k > data[mid]:
    #         self.GetFirstK(data[mid+1:], k)
    #     elif k < data[mid]:
    #         self.GetFirstK(data[:mid], k)
    #     else:
    #         if mid-1:
    #             if data[mid-1] != k:
    #                 return mid
    #             else:
    #                 self.GetFirstK(data[:mid], k)

    def getFirst(self, data, k, stt, end):
        if stt > end:
            return -1
        mid = (stt + end) // 2
        if k == data[mid]:
            if mid and data[mid-1] == k:
                end = mid - 1
            else:
                return mid
        elif k < data[mid]:
            end = mid - 1
        else:
            stt = mid + 1
        return self.getFirst(data, k, stt, end)

    def getLast(self, data, k , stt, end):
        if stt > end:
            return -1
        mid = (stt + end) // 2
        if k == data[mid]:
            if mid+1<len(data) and data[mid + 1] == k:
                stt = mid + 1
            else:
                return mid
        elif k < data[mid]:
            end = mid - 1
        else:
            stt  = mid + 1
        return self.getLast(data, k , stt, end)


# class Solution0:
#     def GetNumberOfK(self, data, k):
#         # write code here
#         number = 0
#         if data != None and len(data) > 0:
#             length = len(data)
#             First = self.GetFirst(data, length, k, 0, length - 1)
#             Last = self.GetLast(data, length, k, 0, length - 1)
#             if First > -1:
#                 number = Last - First + 1
#         return number
#
#     def GetFirst(self, data, length, k, start, end):
#         if start > end:
#             return -1
#         middle = (start + end) // 2
#         if data[middle] == k:
#             if middle > 0 and data[middle - 1] == k:
#                 end = middle - 1
#             else:
#                 return middle
#         elif data[middle] > k:
#             end = middle - 1
#         else:
#             start = middle + 1
#         return self.GetFirst(data, length, k, start, end)


test = [1,2,3,3,3,3,4]
solu = Solution()
print(solu.GetNumberOfK(test, 3))