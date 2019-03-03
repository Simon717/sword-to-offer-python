# -*- coding: utf-8 -*-
"""
   File Name：     36 数组中的逆序对
   Description :
   Author :       simon
   date：          19-2-25
"""

# -*- coding:utf-8 -*-
"""
运行超时
"""
class Solution0:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0

        sortdata = data[:]
        sortdata.sort()
        cnt = 0
        for x in sortdata:
            cnt += data.index(x)
            data.remove(x)
        return cnt

# -*- coding:utf-8 -*-
class Solution1:
    def InversePairs(self, data):
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0]*length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length-1)
        return count
    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start)//2
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count

# -*- coding:utf-8 -*-

"""
始终只能通过50%
"""

class Solution01:
    def InversePairs(self, data):
        if not data:
            return 0

        self.cnt = 0
        self.mergeSort(data)
        return self.cnt % 10000000007

    def mergeSort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        return self.merge(left, right)

    def merge(self, a, b):
        i, j = 0, 0
        res = []
        while i<len(a) and j<len(b):
            if a[i] <= b[j]: # 没有逆序对
                res.append(a[i])
                i += 1
            else: # 存在逆序对
                res.append(b[j])
                j += 1
                self.cnt += len(a)-i
        res += a[i:] # 不会越界吗
        res += b[j:]
        return res

class Solution0:
    def InversePairs(self, data):
        IN = 0
        if len(data) > 1:
            mid = len(data) // 2
            lefthalf = data[:mid]
            righthalf = data[mid:]
            LeftIN = self.InversePairs(lefthalf)
            RightIN = self.InversePairs(righthalf)
            IN = LeftIN + RightIN
            i, j, k = 0, 0, 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j]:
                    data[k] = lefthalf[i]
                    i += 1
                else:
                    IN = IN + len(lefthalf) - i  # 真正计算IN的代码，只有这一行
                    data[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                data[k] = lefthalf[i]
                k += 1
                i += 1
            while j < len(righthalf):
                data[k] = righthalf[j]
                k += 1
                j += 1
        return IN % 10000000007

if __name__ == '__main__':
    test = [1,2,3,4,5,6,0]
    solu = Solution()
    print(solu.InversePairs(test))