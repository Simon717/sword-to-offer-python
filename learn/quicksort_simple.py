# -*- coding: utf-8 -*-
"""
   File Name：     quicksort_simple
   Description :
   Author :       YYJ
   date：          2019-02-22
"""
def quicksort(array):
    size = len(array)
    if not array or size < 2:  # NOTE: 递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)

def test_quicksort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    return quicksort(seq) == sorted(seq)

print("排序", test_quicksort())