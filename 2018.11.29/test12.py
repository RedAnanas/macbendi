n=float(input("请输入第一个数字"))
m=float(input("请输入第二个数字"))
x=input("请输入运算符")
if x=="+" :
    s=n+m
    print(s)
elif x=="-":
    s=n-m
    print(s)
elif x=="*":
    s=n*m
    print(s)
elif x=="/":
    s=n/m
    print(s)
else:
    print("输入有误")
