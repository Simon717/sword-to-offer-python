# -*- coding: utf-8 -*-
"""
   File Name：     io
   Description :
   Author :       simon
   date：          19-3-28
"""

# -- 文件基本操作
output = open(r'C:\spam', 'w')  # 打开输出文件，用于写
input = open('data', 'r')  # 打开输入文件，用于读。打开的方式可以为'w', 'r', 'a', 'wb', 'rb', 'ab'等
fp.read([size])  # size为读取的长度，以byte为单位
fp.readline([size])  # 读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])  # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长。
fp.readable()  # 是否可读
fp.write(str)  # 把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)  # 把seq的内容全部写到文件中(多行一次性写入)
fp.writeable()  # 是否可写
fp.close()  # 关闭文件。
fp.flush()  # 把缓冲区的内容写入硬盘
fp.fileno()  # 返回一个长整型的”文件标签“
fp.isatty()  # 文件是否是一个终端设备文件（unix系统中的）
fp.tell()  # 返回文件操作标记的当前位置，以文件的开头为原点
fp.next()  # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[, whence])  # 将文件打开操作标记移到offset的位置。whence为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。
fp.seekable()  # 是否可以seek
fp.truncate([size])  # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
for line in open('data'):
    print(line)  # 使用for语句，比较适用于打开比较大的文件
with open('data') as file:
    print(file.readline())  # 使用with语句，可以保证文件关闭
with open('data') as file:
    lines = file.readlines()  # 一次读入文件所有行，并关闭文件
open('f.txt', encoding='latin-1')  # Python3.x Unicode文本文件
open('f.bin', 'rb')  # Python3.x 二进制bytes文件
# 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等