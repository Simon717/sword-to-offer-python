# -*- coding: utf-8 -*-
"""
   File Name：     网易 操作序列
   Description :
   Author :       simon
   date：          19-4-9
"""
def helper(nums):
    if nums == [1]:
        return [1]
    return [nums[-1]] + helper(nums[:-1])[::-1]

"""
找规律 [nums[-1], nums[-3], ...., nums[-4],nums[-2]]
"""
def helper2(nums):
    nums = nums[::-1]
    res = ['*'] * len(nums)
    N = len(nums)
    if len(nums) % 2:
        res[len(nums) // 2] = nums[-1]
    q = 0
    for i in range(len(nums)//2):
        res[i] = nums[q]
        res[N-1-i] = nums[q+1]
        q += 2
    return res

"""
发现的另外一种规律
"""
n = int(input().strip())
a = input().strip().split()
b = []
if n % 2 == 0:
    b.extend(a[1::2][::-1])
    b.extend(a[::2])
else:
    b.extend(a[::2][::-1])
    b.extend(a[1::2])
print(' '.join(b))


if __name__ == '__main__':
    _ = input()
    nums = input().strip().split(' ')
    # nums = list(map(int, nums))
    res = helper2(nums)
    # res = list(map(str, res))
    print(' '.join(res))

