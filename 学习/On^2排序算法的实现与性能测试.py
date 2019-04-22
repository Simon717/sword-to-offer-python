# -*- coding: utf-8 -*-
from random import randint
import timeit


"""
插入排序稳定 
相同值的元素的相对顺序在排序前后不会发生变化
"""
# 插入排序
# 左侧已排序 右侧未排序
# 将右侧第一个元素插入到左侧
def insertionSort(alist):
    for i in range(1, len(alist)):
        currentvalue, position = alist[i], i  # 取出当值位置的数值 准备被填充掉, 定义一个指针指向当前数据准备插入的位置
        while alist[position - 1] > currentvalue and position > 0:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue
    return alist

# 希尔排序
# 跨度分组 跨度由大变小最终到1 分组使用插入排序
def shellSort(alist):
    gap = len(alist) // 2 # 组数: gap (跨度) 每组元素个数: 2
    while gap > 0:
        for startpos in range(gap):
            gapInsertionSort(alist, startpos, gap)
        gap = gap // 2
    return alist

"""
希尔排序的辅助函数和插入排序核心代码几乎一样
之前是-1 现在是-gap
"""
def gapInsertionSort(alist, startpos, gap):
    # 希尔排序的辅助函数
    for i in range(startpos + gap, len(alist), gap):
        currentvalue, position = alist[i], i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


# 选择排序
# 左侧已排序 右侧未排序
# 从左往右依次确定每一个位置上应该放置的元素 线性搜索未排序部分的最小值
def selectionSort(alist):
    for i in range(len(alist)):
        minposition = i
        for j in range(i, len(alist)):
            if alist[minposition] > alist[j]:
                minposition = j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist


# 冒泡排序
# 左侧未排序 右侧已排序
# 不断地将最大值放在最右侧
def bubbleSort(alist):
    exchange = False
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist


"""
归并排序
"""
def merge_sort(alist):
        mid = len(alist) // 2
        lefthalf = merge_sort(alist[:mid])
        righthalf = merge_sort(alist[mid:])

        alist = merge(alist, lefthalf, righthalf)
        return alist

def merge(alist, lefthalf, righthalf):
    i, j, k = 0, 0, 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        k += 1
        i += 1
    while j < len(righthalf):
        alist[k] = righthalf[j]
        k += 1
        j += 1

    return alist
if __name__ == '__main__':

    max = 5000
    list = [randint(-max, max) for x in range(max)]
    # 使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
    alist = list[:]
    blist = list[:]
    clist = list[:]
    dlist = list[:]

    '''
    运行次数(number)只能设置成1，因为内存中alist、blist等指向同一个对象，该对象第一次排序后就已经是有序列表了。
    所以在这种情况下会发生有趣的现象。按照短路冒泡排序的性质，它在碰到一个有序列表以后会立刻停止遍历，所以不管它的number是1还是10，time都几乎没变化
    但其他排序方法，就算对有序列表进行排序，交换是不需要了，但是还要遍历&比较，所以他们的运行次数变多的话，time依旧变大
    之前我就是把number设置成100，发现短路冒泡排序简直太快了，才发现这个问题。
    '''
    t1 = timeit.Timer('bubbleSort(alist)', 'from __main__ import bubbleSort,alist')
    print('短路冒泡排序: %s s' % t1.timeit(number=1))

    t2 = timeit.Timer('selectionSort(blist)', 'from __main__ import selectionSort,blist')
    print('选择排序: %s s' % t2.timeit(number=1))

    t3 = timeit.Timer('insertionSort(clist)', 'from __main__ import insertionSort,clist')
    print('插入排序: %s s' % t3.timeit(number=1))

    t4 = timeit.Timer('shellSort(dlist)', 'from __main__ import shellSort,dlist')
    print('希尔排序: %s s' % t4.timeit(number=1))
