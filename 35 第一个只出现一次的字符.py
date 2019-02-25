# -*- coding: utf-8 -*-
"""
   File Name：     35 第一个只出现一次的字符
   Description :
   Author :       simon
   date：          19-2-25
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         # write code here
#         if not s:
#             return
#
#         strlist = list(s)
#         strlist.sort()
#         cnt = 1
#         item = strlist[0]
#         for i in range(1, len(strlist)):
#             if cnt == 1:
#                 if i < len(strlist):
#                     if strlist[i] != item:
#                         return  list(s).index(strlist[i-1])
#             if strlist[i] != item:
#                 cnt = 1
#                 item = strlist[i]
#             else:
#                 cnt += 1
#             if i == len(strlist)-1 and cnt == 1:
#                 return  list(s).index(strlist[i])
#         return -1

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1

        alphabet = {}
        alist = list(s)
        for key in alist:
            if key not in alphabet.keys():
                alphabet[key] = 0
            alphabet[key] += 1
        # for k, v in alphabet.items(): # 本地结果正确 线上结果不正确
        #     if v == 1:
        #         return alist.index(k)
        for i in alist:
            if alphabet[i] == 1:
                return i
        return -1


if __name__ == '__main__':
    test = 'google'
    solu = Solution()
    print(solu.FirstNotRepeatingChar(test))
