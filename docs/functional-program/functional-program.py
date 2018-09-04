# ### 高阶函数(算法函数)
# 
# #### 概念
# 
# 一个函数接收另一个函数作为参数，这种函数就称之为高阶函数。
#%%
def add(x, y, f):
    return f(x) + f(y)


x = -5
y = 6
f = abs

add(x, y, f)
#return 11

# 
# #### map(translate)
# 
# (function, iterable):**注意**,其实就是线性变换
#%%
def f(x):
    return x*x

L = map(f, [1,2,3,4,5,6])

# 一开始以为这样就可以调用，但是实际输出的是什么时候开始调用 <mat at ******>,函数指针，只是构建一个map实例
#%%
list(L)
# lisk 可以用set实例实例化
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
#%%
list(map(str, [1,2,3,4,5,6]))
# 
# #### reduce(reduce, accumulate)
# 
# reduce(function, iterable)把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# **就是降维，就是卷积**
#%%
from functools import reduce
def f(x,y):
    return x*10 +y

reduce(f, [1,2,3,4,5,6])
# 
# #### filter(copy_if)
# 
#%%
list(filter(lambda x:x%2==1, [1,2,3,4,5,6]))

# 把一个序列中的空字符串删掉，可以这么写：
#%%
list(filter(lambda s:s and s.strip() , ['A', '', 'B', None, 'C', '  ']))

# 
# #### sorted(sort)
# 
# 对数列进行排序
#%%
sorted([2,4,-5,1,6,-10,3,5])
sorted([2,4,-5,1,6,-10,3,5],key=abs)
sorted([2,4,-5,1,6,-10,3,5],reverse=True)
# 
# ### 闭包(函数对象)
# 
# 闭包`Closure`相当于c++的函数对象，内部函数可以调用对象的变量和函数，返回值其实就是函数对象的实例化
#%%
def lazy_sum(*args): #函数对象
    def sum():  #相当于函数对象的lambda表达式
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数(lambda)：
#%%
f = lazy_sum(1, 3, 5, 7, 9) # 函数对象实例化１
f2 = lazy_sum(1, 3, 5, 7, 9) # 函数对象实例化２　两个对象之间没有联系
f
f()
#<function lazy_sum.<locals>.sum at 0x101c6ed90>
#25
# 下面来理解这么一个句子
#%%
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
assert (f1() == 9) 
assert (f1() == 9) 
assert (f1() == 9)
# 你以为输出应该是1,3,9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 原作者没有详细的说明这一点，其实用c++的函数对象就好理解多了其实count里面非返回函数部分都是构造函数，调用count的时候就开始调用，
# 这时候i已经变为3了，而之后在调用f()时，调用的i是3,还是不好理解。先回答几个问题:
# - Q1: 返回函数是什么. f()
# - Q2: 闭包的成员变量有几个. A: 2个　　fn, i,很多人会忽略i,这正是出错的原因
# - Q3: 调用count知乎i是几，　A: 3,而且会一直保存着，和fs一样，他们都是成员变量
# 所以到这里答案已经很明显了。上面的三个问题其实也是你在写闭包的时候必须问自己的。如果你有C++基础就当作闭包来写好了。
#
# ### lambda表达式(匿名函数)
# 

# 其实就是lambda表达式,c++也有，不过写法不同，最容易出错的是python的写法没有return.（**注意**自己在使用的时候犯过错）.
# 那么lambda函数要怎么写,先看正常函数的写法。
#%%
def f(x):
    return x * x

# 步骤如下
# - **看成一行**: def f(x): return x * x
# - **去定义** def f():  x: return x*x
# - **去返回** return: 剩下　x: x*x
# - **加lambda**: 如下
#%%
lambda x: x * x
# 
# ### 装饰器(特殊高阶函数)
# 
# 又是一个熟悉的概念，设计模式中行为模式的一种。起到函数的伟哥。冬天里的大棉袄。
#%%
def now():
    print('2015-3-25')
f = now # 可以看成now实例化
f() 

# 函数对象有一个__name__属性，可以拿到函数的名字：
#%%
f.__name__
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
#%%
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper
log(now)()
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
#%%
@log
def hello():
    print("hello worrld")


hello() 
#call now
#2015-3-25
# 把@log放到now()函数的定义处，相当于执行了语句：
#%%
now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
#%%
import functools
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')


now()
#execute now():
#2015-3-25
# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
now.__name__
#'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 或者针对带参数的decorator：
import functools
# 或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func) # wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
# 
# ### 偏函数(对应c++ bind)
#
# 先來看c++11的簡單例子。
# ```cpp
# #include <functional>
# #include <iostream>
#  
# using namespace std;
# using namespace std::placeholders; 
#  
# int product(int a, int b){
#     return a * b;
# }
#  
# int main(){
#     auto product_3 = std::bind(product, _1, 3);
#     cout << product_3(5) << endl;
# }
# ```
def add(a, b):
    return a + b
 
import functools
add_two = functools.partial(add, b=2)
 
print add_two(5)

# python 的例子就比 c++ 简单多了。 从第五行很明显看到 add_two function就是 把 b 的值固定成 2 的 add funcion。