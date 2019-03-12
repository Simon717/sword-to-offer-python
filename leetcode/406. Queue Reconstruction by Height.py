# -*- coding: utf-8 -*-
"""
   File Name：     406. Queue Reconstruction by Height
   Description :
   Author :       simon
   date：          19-3-10
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_h_dict, height, res = {}, [], []
        for pair in people:
            if pair[0] not in people_h_dict:
                people_h_dict[pair[0]] = [pair]
                height.append(pair[0])
            else:
                people_h_dict[pair[0]].append(pair)

        height.sort()
        for h in height[::-1]:
            people_h_dict[h].sort()
            for hh, d in people_h_dict[h]:
                res.insert(d, [hh, d])
        return res


