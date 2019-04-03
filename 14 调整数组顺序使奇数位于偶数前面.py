# -*- coding: utf-8 -*-
"""
   File Name：     14 调整数组顺序使奇数位于偶数前面
   Description :
   Author :       YYJ
   date：          2019-02-15
"""
# -*- coding:utf-8 -*-
class Solution1:
    def reOrderArray(self, array):
        # write code here
        if len(array) == 0:
            return []
        a = [x for x in array if x % 2]
        b = [x for x in array if x % 2 == 0]
        return a+b

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            a,b = 0, len(array)-1
            while a < b:
                while (a<b) and array[a] & 1:
                    a += 1
                while (a<b) and not array[b] & 1:
                    b -= 1
                if a<b:
                    array[a], array[b] = array[b], array[a]
            return array

    def reOrderArray2(self, array):
        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            a,b = 0, len(array)-1
            while a < b:
                while (a<b) and self.isEven(array[a]):
                    a += 1
                while (a<b) and not self.isEven(array[b]):
                    b -= 1
                if a<b:
                    array[a], array[b] = array[b], array[a]
            return array

    def isEven(self, x):
        return x & 1


    def reOrderArray0(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front = 0
        rear = len(array) - 1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array

if __name__ == '__main__':
    testArr = [1,2,3,4]
    solu = Solution()
    print(solu.reOrderArray(testArr))