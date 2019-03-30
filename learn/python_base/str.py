# -*- coding: utf-8 -*-
"""
   File Name：     str
   Description :
   Author :       simon
   date：          19-3-28
"""

# -- 常见字符串常量和表达式
S = ''  # 空字符串
S = "spam’s"  # 双引号和单引号相同
S = "s\np\ta\x00m"  # 转义字符
S = """spam"""  # 三重引号字符串，一般用于函数说明
S = r'\temp'  # Raw字符串，不会进行转义，抑制转义
S = b'Spam'  # Python3中的字节字符串
S = u'spam'  # Python2.6中的Unicode字符串
s1 + s2, s1 * 3, s[i], s[i:j], len(s)  # 字符串操作
'a %s parrot' % 'kind'  # 字符串格式化表达式
'a {1} {0} parrot'.format('kind', 'red')  # 字符串格式化方法
for x in s: print(x)  # 字符串迭代，成员关系
[x * 2 for x in s]  # 字符串列表解析
','.join(['a', 'b', 'c'])  # 字符串输出，结果：a,b,c

# -- 内置str处理函数：
str1 = "stringobject"
str1.upper();
str1.lower();
str1.swapcase();
str1.capitalize();
str1.title()  # 全部大写，全部小写、大小写转换，首字母大写，每个单词的首字母都大写
str1.ljust(width)  # 获取固定长度，左对齐，右边不够用空格补齐
str1.rjust(width)  # 获取固定长度，右对齐，左边不够用空格补齐
str1.center(width)  # 获取固定长度，中间对齐，两边不够用空格补齐
str1.zfill(width)  # 获取固定长度，右对齐，左边不足用0补齐
str1.find('t', start, end)  # 查找字符串，可以指定起始及结束位置搜索
str1.rfind('t')  # 从右边开始查找字符串
str1.count('t')  # 查找字符串出现的次数
# 上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
str1.replace('old', 'new')  # 替换函数，替换old为new，参数中可以指定maxReplaceTimes，即替换指定次数的old为new
str1.strip();  # 默认删除空白符
str1.strip('d');  # 删除str1字符串中开头、结尾处，位于 d 删除序列的字符
str1.lstrip();
str1.lstrip('d');  # 删除str1字符串中开头处，位于 d 删除序列的字符
str1.rstrip();
str1.rstrip('d')  # 删除str1字符串中结尾处，位于 d 删除序列的字符
str1.startswith('start')  # 是否以start开头
str1.endswith('end')  # 是否以end结尾
str1.isalnum(); # alpha numeric 数字 or 字符
str1.isalpha();
str1.isdigit();
str1.islower();
str1.isupper()  # 判断字符串是否全为字符、数字、小写、大写

# -- 三重引号编写多行字符串块，并且在代码折行处嵌入换行字符\n
mantra = """hello world
            hello python
            hello my friend"""
# mantra为"""hello world \n hello python \n hello my friend"""

# -- 索引和分片：
S[0], S[len(S)–1], S[-1]  # 索引
S[1:3], S[1:], S[:-1], S[1:10:2]  # 分片，第三个参数指定步长，如`S[1:10:2]`是从1位到10位没隔2位获取一个字符。

# -- 字符串转换工具：
int('42'), str(42)  # 返回(42, '42')
float('4.13'), str(4.13)  # 返回(4.13, '4.13')
ord('s'), chr(115)  # 返回(115, 's')
int('1001', 2)  # 将字符串作为二进制数字，转化为数字，返回9
bin(13), oct(13), hex(13)  # 将整数转化为二进制/八进制/十六进制字符串，返回('0b1101', '015', '0xd')

# -- 另类字符串连接
name = "wang" "hong"  # 单行，name = "wanghong"
name = "wang" \
       "hong"  # 多行，name = "wanghong"

# -- Python中的字符串格式化实现1--字符串格式化表达式
"""
基于C语言的'print'模型，并且在大多数的现有的语言中使用。
通用结构：%[(name)][flag][width].[precision]typecode
"""
"this is %d %s bird" % (1, 'dead')  # 一般的格式化表达式
"%s---%s---%s" % (42, 3.14, [1, 2, 3])  # 字符串输出：'42---3.14---[1, 2, 3]'
"%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)  # 对齐方式及填充："1234...  1234...1234  ...001234"
x = 1.23456789
"%e | %f | %g" % (x, x, x)  # 对齐方式："1.234568e+00 | 1.234568 | 1.23457"
"%6.2f*%-6.2f*%06.2f*%+6.2f" % (x, x, x, x)  # 对齐方式：'  1.23*1.23  *001.23* +1.23'
"%(name1)d---%(name2)s" % {"name1": 23, "name2": "value2"}  # 基于字典的格式化表达式
"%(name)s is %(age)d" % vars()  # vars()函数调用返回一个字典，包含了所有本函数调用时存在的变量

# -- Python中的字符串格式化实现2--字符串格式化调用方法
# 普通调用
"{0}, {1} and {2}".format('spam', 'ham', 'eggs')  # 基于位置的调用
"{motto} and {pork}".format(motto='spam', pork='ham')  # 基于Key的调用
"{motto} and {0}".format('ham', motto='spam')  # 混合调用
# 添加键 属性 偏移量 (import sys)
"my {1[spam]} runs {0.platform}".format(sys, {'spam': 'laptop'})  # 基于位置的键和属性
"{config[spam]} {sys.platform}".format(sys=sys, config={'spam': 'laptop'})  # 基于Key的键和属性
"first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C'])  # 基于位置的偏移量
# 具体格式化
"{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)  # 输出'3.141590e+00, 3.142e+00, 3.14159'
"{fieldname:format_spec}".format(......)
# 说明:
"""
    fieldname是指定参数的一个数字或关键字, 后边可跟可选的".name"或"[index]"成分引用
    format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
    fill        ::=  <any character>              #填充字符
    align       ::=  "<" | ">" | "=" | "^"        #对齐方式
    sign        ::=  "+" | "-" | " "              #符号说明
    width       ::=  integer                      #字符串宽度
    precision   ::=  integer                      #浮点数精度
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
# 例子:
'={0:10} = {1:10}'.format('spam', 123.456)  # 输出'=spam       =    123.456'
'={0:>10}='.format('test')  # 输出'=      test='
'={0:<10}='.format('test')  # 输出'=test      ='
'={0:^10}='.format('test')  # 输出'=   test   ='
'{0:X}, {1:o}, {2:b}'.format(255, 255, 255)  # 输出'FF, 377, 11111111'
'My name is {0:{1}}.'.format('Fred', 8)  # 输出'My name is Fred    .'  动态指定参数