# -*- coding: utf-8 -*-
"""
   File Name：     29 数组中出现次数超过一半的数字
   Description :
   Author :       YYJ
   date：          2019-02-21
"""

# -*- coding:utf-8 -*-
"""
如果存在满足条件的数 这个数只能是这个数组的中位数
利用快速排序找到中位数 检验中位数是否过半
"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        length = len(numbers)
        if length == 1:
            return numbers[0]

        # 找到数组中位数
        middle = length >> 1
        middleNum = self.findK(numbers, middle)

        if not self.CheckMoreThanHalf(middleNum):
            return 0
        return middleNum

    def findK(self, nums, K):
        pass

    def Partition(self, nums, ):
        pass


class Solution0:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0

        # 快速排序找到中位数
        middle = length >> 1
        result = self.findK(numbers, middle)

        # 检验是否过半
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

    def findK(self, numbers, K):
        length = len(numbers)
        start = 0
        end = length - 1
        index = self.Partition(numbers, length, start, end)
        while index != K:
            if index > K:
                end = index - 1
                index = self.Partition(numbers, length, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, length, start, end)
        return numbers[K]

        # 划分算法
    def Partition(self, numbers, length, start, end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None
        if end == start:
            return end
        """
        始终维护条件： arr[l+1...i) <= v; arr(j...r] >= v
        所以算法停止时 i处于>=v部分的第一个元素 j处于<=v部分的最后一个元素
        测试样例： [3,4,2,5,1] 最终停止：[3][1,2][5,4] right指向2 left指向5 
                    此时left-right==1 恰好将除标定点之外的数据分为两个部分
        """
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end


        while True:
            while leftmark <= rightmark and numbers[leftmark] < pivotvlue:
                leftmark += 1
            while leftmark <= rightmark and numbers[rightmark] > pivotvlue:
                rightmark -= 1

            if leftmark > rightmark:
                break
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
                leftmark += 1
                rightmark -= 1

        # 最终情况是leftmark指向第一个>=部分 rightmark指向最后一个<=部分
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark

        # 检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid

        # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True

if __name__ == '__main__':
    test = [3,2,2,2,3]
    solu = Solution0()
    print(solu.MoreThanHalfNum_Solution(test))
    print(test)