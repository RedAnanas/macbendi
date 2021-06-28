#1.输入两个数，输出较大的数。
'''
a=int(input("请输入第一个数"))
b=int(input("请输入第二个数"))
if a>b:
    print (a)
else:
    print (b)
'''
#2.输入两个数，如果a大于b且b>20则输出a+b，如果a<b或a为负数则输出a-b，其他情况输出a*b
'''
a=int(input("请输入第一个数"))
b=int(input("请输入第二个数"))
if a>b and b>20:
    print(a+b)
elif a<b or a<0:
    print(a-b)
else:
    print(a*b)
'''
#3.输入一个字符，如果它是一个大写字母,则把它变成小写输出,如果是小写,则变成大写输出,
#其他字符不变输出。
"""
a=input("请输入一个字符")
b=ord(a)
if b>=65 and b<=90:
    print(a.lower())
elif b>=97 and b<=122:
    print(a.upper())
else:
    print(a)
"""
#4.分别输入年、月、日，判断此日期是当年的第几天。
'''
ping=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
run=[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
while True:
    y=int(input("请输入一个年份（1980-2099）:"))
    m=int(input("请输入一个月份（1-12）:"))
    d=int(input("请输入一个日:"))
    if y>=1980 and y<=2099:
        if (y%4==0 and y%100!=0) or y%400==0:
            sumday=run[m-1]+d
            print("是闰年,是当年的第%d天"%sumday)
            
            break
        else:
            sumday=ping[m-1]+d
            print("是平年,是当年的第%d天"%sumday)
            break
    else:
        print("错误年份，请重新输入")
        continue
'''
#5.打印99乘法表。
'''
for i in range(1,10,1):
    for j in range(1,i+1,1):
        print("%d*%d=%d "%(j,i,j*i),end="",sep="")
    print("")
'''
#6.一个10000以内整数，它加上100和加上268后都是一个完全平方数，请
#问该数是多少？（提示：用到math模块）
'''
import math
for i in range (-100,10001):
   m=int(math.sqrt(i+100))
   n=int(math.sqrt(i+268))
   if m*m==i+100 and n*n==i+268:
       print("这个数是：%d"%i)
'''
#7.输入三个整数x,y,z，请把这三个数由小到大输出。
'''
x=int(input("请输入第x个整数"))
y=int(input("请输入第y个整数"))
z=int(input("请输入第z个整数"))

if x>y and y>z:
    print("%d>%d>%d"%(x,y,z))
elif x>y and z>y and x>z:
    print("%d>%d>%d"%(x,z,y))   
elif y>x and x>z:
    print("%d>%d>%d"%(y,x,z))
elif y>x and z>x and y>z:
    print("%d>%d>%d"%(y,z,x))    
elif z>x and x>y:
    print("%d>%d>%d"%(z,x,y))
elif z>x and y>x and z>y:
    print("%d>%d>%d"%(z,y,x))
else:
    print("错误")
'''

#8.求1000以内的水仙花数。
#提示：如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
"""
for i in range(100,1000):
    a=i%10
    b=(i%100-a)/10
    c=(i-b*10-a)/100
    n=a**3+b**3+c**3
    if n==i:
        print("%d是一个水仙花数"%i)
"""
#9.对3、65、22、102、4进行升序排序。
"""
a=[3,65,22,102,4]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            b=a[j]
            a[j]=a[j+1]
            a[j+1]=b
print(a)
"""         

#10.猜数字游戏，系统随机生成一个1000以内的数字，用户输入一个数字，
#如果输入数字大于系统数字则提示‘大了’，反之提示‘小了’，直到相
#等游戏结束，提示‘通关’ 并输出猜测次数。（提示：用到random模块）
"""
import random
x=random.randint(1,1000)
i=0
while True:
    a=int(input("请输入一个1-1000的数"))
    i=i+1
    if a>x:
        print("大了")
    elif a<x:
        print("小了")
    else:
        print("通关！猜测次数为：%d"%i)
        break
""" 
#11.打印直角三角形设定的总行数line可以随机修改，修改后仍然能打印出line行的直角三角形。
"""
line=6
for i in range(1,line,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print("\t")
"""
#12.打印等腰三角形：
'''
line=6
for i in range(1,line,1):
    for k in range(0,line-i,1):
        print(" ",end="")
    for j in range(0,2*i-1,1):
        print("*",end="")
    print("\t")
'''


    
