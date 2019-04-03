# -*- coding: utf-8 -*-
"""
   File Name：     华为 蛇形字符串
   Description :
   Author :       simon
   date：          19-3-20
"""
def solu(s):
    s = list(s)
    ss = []
    letters = "abcdefghijklmnopqrstuvwxyz"

    for i in s:
        if i.lower() in letters:
            ss.append(i)
    ss.sort() # 原地操作
    lower = []
    upper = []
    for i in ss:
        if i in letters:
            lower.append(i)
        else:
            upper.append(i)
    merge = []
    p1, p2 = 0, 0
    while p1 < len(lower) and p2 < len(upper):
        if lower[p1] >= upper[p2].lower():
            merge.append(upper[p2])
            p2 += 1
        else:
            merge.append(lower[p1])
            p1 += 1
    if p1 == len(lower):
        merge += upper[p2:]
    else:
        merge += lower[p1:]

    p1 = p2 = 0
    maxlen = 0
    res = []
    reslen = []
    while len(merge):
        p1 = p2 = 0
        maxlen = 0
        cur = []
        while p1 < len(merge)-1:
            if ord(merge[p1]) - ord(merge[p1+1]) == 26:
                i = 1
                while ord(merge[p2]) - ord(merge[p2+1]) == 26 and ord(merge[p2]) - ord(merge[p1])==i:
                    i += 1
                    p2 += 2
                curlen = (p2 - p1) // 2
                if curlen > maxlen:
                    maxlen = curlen
                    cur = [p1, p2]
                # res.append(merge[p1:p2])
                # reslen.append((p2 - p1) // 2)
            else:
                p1 += 1
                p2 += 1
        res.append(merge[p1:p2])
        for ii in range(p1, p2): # TODO
            merge.pop(ii)
    return res

"""
本题思路： 
1. 从输入字符串中过滤出我们需要的英文字母 按照大小写分离成两个部分 之后排序
2. 首先只考虑大写字母（相应的小写字母是否存在只需要加上一行判断语句即可） 将问题转化为一个排序的字符串中找到最长的连续字符串
3. 对于连续字符串问题 利用双指针思想 p1指向连续子序列的首字母 p2指向未字母 
    这里我体会到 while 循环和for循环的不同之处和相同之处 while循环的有点在于一次性可以进行多重判断 因为这个问题的判断条件就是多重判断 所以while循环很方便
    在每一次循环结束时人为加上index++ 跟for循环没有区别 for循环只是在固定循环次数的时候比较好用 当然可以用break短路
    之前一直把while循环和if弄混.. 醉了

Python
"""
class Solution:
    def she(self, s):
        s = list(s)
        upper, lower = [],  []
        for i in s:
            if ord('a') <= ord(i) <= ord('z'):
                lower.append(i)
            if ord('A') <= ord(i) <= ord('Z'):
                upper.append(i)
        upper.sort()
        lower.sort()
        res = []

        while upper:
            p1, p2 = 0, 0   # 某一轮搜索
            step_maxlen = 0
            step_res = []
            while p1 < len(upper):  # 考察不同起点
                if upper[p1].lower() in lower:
                    p2 = p1 + 1
                    p2Front = p1 # 定位到尾指针的前一个元素
                    temp_res = [upper[p1]] # 以当前节点的作为起点的最长连续字符
                    while p2 < len(upper) and (ord(upper[p2]) - ord(upper[p2Front]) in [0, 1]) and upper[p2].lower() in lower: # 考察不同的终点
                        if ord(upper[p2]) - ord(upper[p2Front]) == 1:
                            temp_res.append(upper[p2])
                            p2Front = p2
                        p2 += 1
                    if len(temp_res) > step_maxlen:
                        step_maxlen = len(temp_res)
                        step_res = temp_res
                else: # 找不到小写字符直接删除
                    upper.remove(upper[p1])
                p1 += 1
            # 处理当前step得到的结果 并且删除掉已经使用了的字符
            stepp = ''
            for x in step_res:
                stepp += x + x.lower()
                upper.remove(x)
                lower.remove(x.lower())
            res.append(stepp)
        return res

    def hashSolu(self, s):
        upper, lower = {}, {}
        for i in s:
            if ord('A') <= ord(i) <= ord('Z'):
                if i not in upper.keys():
                    upper[i] = 0
                upper[i] += 1
            if ord('a') <= ord(i) <= ord('z'):
                if i not in lower.keys():
                    lower[i] = 0
                lower[i] += 1

         self.dropUp(upper, lower)

        while upper:
            up_list = self.getUpList(upper)
            maxlenUp = self.getMaxUp(up_list)




    def dropUp(self, up, low):
        return

    def getUpList(self, up):
        return


"""

"""


if __name__ == '__main__':

    # test = 'Aa'
    # test = 'OoPpBCccbAa'
    test = 'SxxxsrR*AaAaBbSsSs'
    solu1 = Solution()
    print(solu1.she(test))

