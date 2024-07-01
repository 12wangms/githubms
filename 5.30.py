# def fun1(x,y):
#     print("这是函数一")
#     sum=x+y
#     return sum
#
# def fun2():
#     print("这是函数二")
#     sum=fun1(2,3)
#     print(sum)
# fun2()

# def max(x,y):
#     return x if x>y else y
# print(max(888,9))


# def maxs(a,b,c,d):
#     res1=max(a,b)
#     res2=max(res1,c)
#     res3=max(res2,d)
#     return res3
# print(maxs(5,9,6,2000))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num=5
# result=factorial(num)
# print(f"The factorial of {num} is:{result}")

#猴子吃桃

# #天数
# n=int(input("请输入猴子摘桃的天数：\n"))
# #函数体
# def F(x):
#     if x==1:
#         return x #为边界
#     else:
#         return (F(x-1)+1)*2 #递归函数
# print(F(n))