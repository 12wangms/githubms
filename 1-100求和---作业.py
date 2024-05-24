#方法一
sum2=0
for i in range(1,101):
    sum2+=i
print("---sum1---")
print(sum2)

#方法二
def fsum(n):
    s=0
    for i in range(1,n+1):
       s+=i
    print(s)
print("----sum2----")
fsum(100)


#方法三while循环实现
def fsum1(n):
    i=0 #初始化变量
    s=0
    while i < n+1: #条件判断
        s +=i #循环体
        i +=1 #改变变量
    print(s)
print("----sum3----")
fsum1(100)

#方法四递归的思路
def fsum2(n):
    if n==1:
        return 1
    else:
        return n+fsum2(n-1)
print("----sum4----")
print(fsum2(100))

#方法五一句代码搞定
print("----sum5----")
print(sum(list(range(1,101))))

#方法六：使用Python的reduce函数（需要安装functools库）

#!/usr/bin/python
#coding:utf-8
#author:菜就多练呀
from functools import reduce
def add(x, y):
    return x + y
total = reduce(add, range(1, 101))
print("----Sum6 Total----")
print(total)