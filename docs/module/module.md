## 使用模块


```python
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
' a test module '
__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```

**命令行**运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

### 作用域
 
在Python中，是通过_前缀来实现的
- **xxx public** abc,x123,PI
- **__xxx__ 特殊变量** : __author__，__name__, __doc__
- **_xxx private **: _abc, __abc

#  安装第三方模块
## 模块搜索路径 　

搜索当前目录、所有已安装的内置模块和第三方模块,搜索路径存放在sys模块的path变量


```python
#%%
import sys
sys.path
#['',
#'/opt/ros/kinetic/lib/python2.7/dist-packages',
#'/home/syue/anaconda3/lib/python36.zip',
#'/home/syue/anaconda3/lib/python3.6',
#'/home/syue/anaconda3/lib/python3.6/lib-dynload',
#'/home/syue/anaconda3/lib/python3.6/site-packages',
#'/home/syue/anaconda3/lib/python3.6/site-packages/notedown-1.5.0-py3.6.egg',
#'/home/syue/anaconda3/lib/python3.6/site-packages/pandoc_attributes-0.1.7-py3.6.egg',
#'/home/syue/anaconda3/lib/python3.6/site-packages/IPython/extensions',
#'/home/syue/.ipython']
```

如果我们要添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录：


```python
#%%
import sys
sys.path.append('/Users/michael/my_py_scripts')
sys.path
```

这种方法是在运行时修改，运行结束后失效。
第二种方法是设置环境变量`PYTHONPATH`，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。


```python

```

