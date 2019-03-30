# -*- coding: utf-8 -*-
"""
   File Name：     listdict
   Description :
   Author :       simon
   date：          19-3-28
"""

""" 
列表 
"""
# -- 常用列表常量和操作
L = [[1, 2], 'string', {}]  # 嵌套列表
L = list('spam')  # 列表初始化
L = list(range(0, 4))  # 列表初始化
list(map(ord, 'spam'))  # 列表解析
len(L)  # 求列表长度
L.count(value)  # 求列表中某个值的个数
L.append(obj)  # 向列表的尾部添加数据，比如append(2)，添加元素2
L.insert(index, obj)  # 向列表的指定index位置添加数据，index及其之后的数据后移
L.extend(interable)  # 通过添加iterable中的元素来扩展列表，比如extend([2])，添加元素2，注意和append的区别
L.index(value, [start, [stop]])  # 返回列表中值value的第一个索引
L.pop([index])  # 删除并返回index处的元素，默认为删除并返回最后一个元素
L.remove(value)  # 删除列表中的value值，只删除第一次出现的value的值
L.reverse()  # 反转列表
L.sort(cmp=None, key=None, reverse=False)  # 排序列表
a = [1, 2, 3], b = a[10:]  # 注意，这里不会引发IndexError异常，只会返回一个空的列表[]
a = [], a += [1]  # 这里实在原有列表的基础上进行操作，即列表的id没有改变
a = [], a = a + [1]  # 这里最后的a要构建一个新的列表，即a的id发生了变化

# -- 用切片来删除序列的某一段
a = [1, 2, 3, 4, 5, 6, 7]
a[1:4] = []  # a = [1, 5, 6, 7]
a = [0, 1, 2, 3, 4, 5, 6, 7]
del a[::2]  # 去除偶数项(偶数索引的)，a = [1, 3, 5, 7]


"""
 字典 
"""
# -- 常用字典常量和操作
D = {}
D = {'spam': 2, 'tol': {'ham': 1}}  # 嵌套字典
D = dict.fromkeys(['s', 'd'], 8)  # {'s': 8, 'd': 8}
D = dict(name='tom', age=12)  # {'age': 12, 'name': 'tom'}
D = dict([('name', 'tom'), ('age', 12)])  # {'age': 12, 'name': 'tom'}
D = dict(zip(['name', 'age'], ['tom', 12]))  # {'age': 12, 'name': 'tom'}
D.keys();
D.values();
D.items()  # 字典键、值以及键值对
D.get(key, default)  # get函数
D.update(D_other)  # 合并字典，如果存在相同的键值，D_other的数据会覆盖掉D的数据
D.pop(key, [D])  # 删除字典中键值为key的项，返回键值为key的值，如果不存在，返回默认值D，否则异常
D.popitem()  # pop字典中随机的一项（一个键值对）
D.setdefault(k[, d])  # 设置D中某一项的默认值。如果k存在，则返回D[k]，否则设置D[k]=d，同时返回D[k]。
del D  # 删除字典
del D['key']  # 删除字典的某一项
if key in D:   if
key not in D:  # 测试字典键是否存在
# 字典注意事项：（1）对新索引赋值会添加一项（2）字典键不一定非得是字符串，也可以为任何的不可变对象
# 不可变对象：调用对象自身的任意方法，也不会改变该对象自身的内容，这些方法会创建新的对象并返回。
# 字符串、整数、tuple都是不可变对象，dict、set、list都是可变对象
D[(1, 2, 3)] = 2  # tuple作为字典的key

# -- 字典解析
D = {k: 8 for k in ['s', 'd']}  # {'s': 8, 'd': 8}
D = {k: v for (k, v) in zip(['name', 'age'], ['tom', 12])}  # {'age': 12, 'name': tom}


# -- 字典的特殊方法__missing__：当查找找不到key时，会执行该方法
class Dict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


dct = dict()
dct["foo"].append(1)  # 这有点类似于collections.defalutdict
dct["foo"]  # [1]

"""
元组
"""
# -- 元组和列表的唯一区别在于元组是不可变对象，列表是可变对象
a = [1, 2, 3]  # a[1] = 0, OK
a = (1, 2, 3)  # a[1] = 0, Error
a = ([1, 2])  # a[0][1] = 0, OK
a = [(1, 2)]  # a[0][1] = 0, Error

# -- 元组的特殊语法: 逗号和圆括号
D = (12)  # 此时D为一个整数 即D = 12
D = (12,)  # 此时D为一个元组 即D = (12, )


"""
集合
"""
# -- 集合set
"""
set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
set支持union(联合), intersection(交), difference(差)和symmetric difference(对称差集)等数学运算。
set支持x in set, len(set), for x in set。
set不记录元素位置或者插入点, 因此不支持indexing, slicing, 或其它类序列的操作
"""
s = set([3, 5, 9, 10])  # 创建一个数值集合，返回{3, 5, 9, 10}
t = set("Hello")  # 创建一个唯一字符的集合返回{}
a = t | s;
t.union(s)  # t 和 s的并集
b = t & s;
t.intersection(s)  # t 和 s的交集
c = t – s;
t.difference(s)  # 求差集（项在t中, 但不在s中）
d = t ^ s;
t.symmetric_difference(s)  # 对称差集（项在t或s中, 但不会同时出现在二者中）
t.add('x');
t.remove('H')  # 增加/删除一个item
s.update([10, 37, 42])  # 利用[......]更新s集合
x in s, x not in s  # 集合中是否存在某个值
s.issubset(t);
s <= t  # 测试是否 s 中的每一个元素都在 t 中
s.issuperset(t);
s >= t  # 测试是否 t 中的每一个元素都在 s 中
s.copy();
s.discard(x);  # 删除s中x
s.clear()  # 清空s
{x ** 2 for x in [1, 2, 3, 4]}  # 集合解析，结果：{16, 1, 4, 9}
{x for x in 'spam'}  # 集合解析，结果：{'a', 'p', 's', 'm'}

# -- 集合frozenset，不可变对象
"""
set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
frozenset是不可变对象，即存在hash值，可作为字典的键值
frozenset对象没有add、remove等方法，但有union/intersection/difference等方法
"""
a = set([1, 2, 3])
b = set()
b.add(a)  # error: set是不可哈希类型
b.add(frozenset(a))  # ok，将set变为frozenset，可哈希