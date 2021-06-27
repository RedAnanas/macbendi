#1.输入三角形的三条边，判断是否能组成三角形；如果可以组成三角形，
#判断是等边三角形、等腰三角形、直角三角形、等腰直角三角形还是普通三角形；
"""
a=float(input("请输入三角形的第一条边："))
b=float(input("请输入三角形的第二条边："))
c=float(input("请输入三角形的第三条边："))
if a+b>c and a+c>b and b+c>a:
    print("可以组成三角形")
    if a==b==c:
        print("是等边三角形")
    elif a==b or b==c or a==c:
        print("是等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print("是直角三角形")
        if a==b or b==c or a==c:
            print("是等腰直角三角形")
    else:
        print("是普通三角形")
else:
    print("不能组成三角形")
"""
#2.电脑随机生成一个0-100之间的整数，进行猜数游戏，大了提示大了，小了提示小了，
#直至猜测成功，并输出猜测的次数；
"""
import random
x=random.randint(1,100)
i=0
while True:
    a=int(input("请输入一个1-100的整数"))
    i=i+1
    if a>x:
        print("大了")
    elif a<x:
        print("小了")
    else:
        print("恭喜你猜对了,猜测次数为：%d"%i)
        break
"""  
#3.输入一个手机号码，进行以下验证：
#（1）只能是数字；
#（2）长度为11位；
#（3）根据前3位判断是属于电信、联通还是移动号码；
#如果输入错误，可以重新输入；
"""
while True:
    a=input("请输入一个手机号")
    d=[133,149,153,173,177,180,181,189,199]
    l=[130,131,132,145,155,156,166,171,175,176,185,186,166]
    y=[134,135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198]
    if it(a.isdig) and len(a)==11:
        if int(a[0:3]) in d: 
            print("是电信号码")
            break
        elif int(a[0:3]) in l:
            print("是联通号码")
            break
        elif int(a[0:3]) in y:
            print("是移动号码")
            break
        else:
            print("是一个错误的号码，请重新输入")
            continue
    else:
        print("输入错误，请重新输入")
        continue
"""    
#4.从键盘输入年份，进行必要的验证后判断是否是闰年；
"""
while True:
    a=input("请输入一个年份（1980-2099）:")
    if a.isdigit() and int(a)>=1980 and int(a)<=2099:
        if (int(a)%4==0 and int(a)%100!=0) or int(a)%400==0:
            print("是闰年")
            break
        else:
            print("是平年")
            break
    else:
        print("错误年份，请重新输入")
        continue
"""

#5.输出1000以内的质数；*********
"""
for i in range(1,99):
    for j in range(2,100):
        if i%j==0  :
            print("质数为：%d"%j)
            break
"""
#6.计算输入的数字的阶乘；10 10*9*8
"""
n=int(input("请输入一个数字"))
a=1
for i in range(1,n+1):   
    a=a*i
print(a)
"""
#7.输出30位斐波那契数列；1,1,2,3,5,8,13,21,34,55,89
"""
lis=[]
for i in range(30):
    if i==0 or i==1:
        lis.append(1)
    else:
        lis.append(lis[i-2]+lis[i-1])
print(lis)
"""    
#8.对一个数组进行冒泡排序

a=[7,6,5,4,3,2,1]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            b=a[j]
            a[j]=a[j+1]
            a[j+1]=b
    print(a)


#9.使用原生方法完成向列表中插入一个元素
"""
a=["asd","asdsa","12312","123","sad123"]
b=["123456"]
a=a+b
print(a)
"""




