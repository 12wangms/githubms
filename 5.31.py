#from datetime import date
#
# a = date.today()
# print(a)
# print(a.year)
# print(a.month)
# print(a.day)
# a=date(2017,3,1)
# b=date(2017,3,15)
# print(a.__eq__(b))
# print(a.__ge__(b))
# print(a.__gt__(b))
# print(a.__le__(b))
# print(a.__lt__(b))
# print(a.__ne__(b))
# print(a.__sub__(b))
# print(a.__rsub__(b))
#
# print(a.__format__('%Y-%m-%d'))
# print(a.__format__('%Y/%m/%d'))
# print(a.__format__('%y-%m-%d'))
# print(a.__format__('%D'))
# print(a.__format__('%d'))
# print(a.__format__('%m'))
# print(a.__format__('%M'))

# from datetime import time
# a=time(12,20,30,899)
# print(a)
# print(a.__format__('%H:%M:%S'))

# from datetime import *
# d= date(2012,12,12)
# print(d)
# #昨天
# d1= d+ timedelta(days=-1)
# print(d1)
# #明天
# d2= d+ timedelta(days=1)
# print(d2)

# from  datetime import *
# dt = datetime(2012,12,12,23,59,59)
# print(dt)
# #昨天
# dt1=dt+timedelta(days=-1)
# #明天
# dt2=dt+timedelta(days=1)
# #上一个小时
# dt3=dt+timedelta(hours=-1)
# #下一个小时
# dt4=dt+timedelta(hours=1)
# #上一秒
# dt5=dt+timedelta(seconds=-1)
# #下一秒
# dt6=dt+timedelta(seconds=1)
#
# print(dt1)
# print(dt2)
# print(dt3)
# print(dt4)
# print(dt5)
# print(dt6)


# import time
#
# a = time.time()
# for x in range(100000):
#     pass
# b=time.time()-a
# print(b)
# #第一次调用，返回程序实际的运行时间
# print(time.perf_counter())
# #第二次调用，返回的是距离上一次调用的时间隔
# print(time.perf_counter())
# #第三次调用，
# print(time.perf_counter())
#
# print(time.gmtime())
#
# print(time.localtime())
# a=time.time()
# time.localtime(a)
#
# #sleep(s)功能：执行程序时，暂停给定数秒，s为秒数。
# print("stat:%s"%time.ctime())
# time.sleep(5)
# print("End:%s"%time.ctime())
#
# print(time.time())
# print(time.ctime(time()))

# import time
# a=time.strftime("%Y-%m-%d",time.gmtime())
# print(a)
# b=time.strftime("%Y-%m-%d %X")
# print(b)
# c=time.strftime("%x %X")
# print(c)

#calendar模块
import calendar
thismonth=calendar.month(2021,11,0)
print(thismonth)

#isleap()方法是判断年份为润年还是平年
#2018是平年，所以为false
print(calendar.isleap(2018))
#2008是润年，所以为True
print(calendar.isleap(2008))