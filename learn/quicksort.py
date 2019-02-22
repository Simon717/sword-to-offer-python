# -*- coding: utf-8 -*-
"""
   File Name：     quicksort
   Description :
   Author :       YYJ
   date：          2019-02-22
"""

def partition(numbers, start, end):
    pivot = numbers[start]
    left = start + 1
    right = end

    while True:
        while left <= right and numbers[left] < pivot:
            left += 1

        while right >= left and numbers[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    numbers[start], numbers[right] = numbers[right], numbers[start]
    return right


def partition0(alist, first, last):
    # rand = randint(first, last)
    # alist[first], alist[rand] = alist[rand], alist[first]
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    while True:
        while leftmark <= rightmark and alist[leftmark] < pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] > pivotvalue:
            rightmark -= 1

        if leftmark > rightmark:
            break
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            leftmark += 1 # 这两行代码必须有 否则程序可能死循环 测试样例 [3,2,2,2,3]
            rightmark -= 1

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark

# bug代码 测试样例 [3, 2, 2, 2, 3]
def Partition(numbers, start, end):
    pivot = numbers[start]
    left = start + 1
    right = end

    while True:
        while left <= right and numbers[left] <= pivot :
            left += 1
        while left <= right and numbers[right] >= pivot :
            right -= 1

        if left > right:
            break
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    numbers[right], numbers[start] = numbers[start], numbers[right]
    return right

def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l))

if __name__ == '__main__':
    test = [3, 2, 2, 2, 3]
    print(Partition(test, 0, len(test)-1))
    print(test)