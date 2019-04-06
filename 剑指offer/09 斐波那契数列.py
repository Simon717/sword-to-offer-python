# -*- coding: utf-8 -*-
"""
   File Name：     09 斐波那契数列
   Description :
   Author :       YYJ
   date：          2019-02-14
"""

# -*- coding:utf-8 -*-
"""
运行时间：29ms

占用内存：5864k
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        if n < 2:
            return res[n]
        else:
            a, b = 0, 1
            # i = 1
            # while i < n:
            #     a, b = b, a+b
            #     i += 1

            # use for loop
            for _ in range(n-1):
                a, b = b, a + b
            return b

    def jumpFloor(self, number):
        res = [1,2]
        if number < 3:
            return res[number-1]
        else:
            a,b = 1,2
            for _ in range(number-2):
                a, b = b, a+b
            return b

    def jumpFloorII(self, number):
        # write code here
        return 2 ** (number - 1)


# write code here


class Solution2:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1] # 交替赋值 节省一般的赋值操作
        return tempArray[n%2]

    # 青蛙跳台阶, 每次可以跳1级或2级
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]

    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.Fibonacci(3))
    print(solu.jumpFloor(3))

    # test = Solution2()
    # print(test.Fibonacci(100))
    # print(test.jumpFloor(3))
    # print(test.jumpFloorII(3))