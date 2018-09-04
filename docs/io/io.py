# ## 文件读写
# Python内置了读写文件的函数，用法和C是兼容的。
# 
# ### 读文件
# 
# 
# #### 不安全版
# 
#%%
file = '/home/syue/github/python-notes/docs/io/test.txt'
f = open(file, 'r')
print(f.read())
f.close()

# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
# 最后一步是调用close()方法关闭文件
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# 
# #### 安全版
# 
#%% 
try:
    f = open(file, 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 
# #### 简洁版
# 
#%%
with open(file, 'r') as f:
    print(f.read())
 
 
# **注意**: 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 
# #### 多行版
# 
#%%
with open(file, 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

# 
# ### 写文件
# 
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# #### 覆盖版
#%%
with open(file, 'w') as f:
    f.write("aaaa")

with open(file, 'r') as f:
    print(f.read())


# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
# 
# #### 追加版
#  
# 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。(以a替代w)
#%%
with open(file, 'a') as f:
    f.write("aaaa")

with open(file, 'r') as f:
    print(f.read())


# 
# ## 操作文件和目录
# 
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
# ## 环境变量
#%%
import os
os.environ
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
os.environ.get('PATH')
#...

# ## 系统信息
#%%
import os
os.name # 操作系统类型
#'posix'
os.uname()
# 查看当前目录的绝对路径:
os.path.abspath('.')
#'/$path'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
#'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')