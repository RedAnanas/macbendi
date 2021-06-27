#1.输入一个半径，计算出圆的周长和面积。
"""
r=float(input("请输入半径"))
c=2*3.14*r
s=3.14*r**2
print("周长为:%f,面积为:%f"%(c,s))
"""
#2.输入两个数字a，b，计算a与b之和与a与b之差的乘积。
"""
a=int(input("请输入数字a"))
b=int(input("请输入数字b"))
c=(a+b)*(a-b)
print("a与b之和与a与b之差的乘积为：%d"%c)
"""
#3.输入两个数字a和b，计算出a的b次方再除以b取整后的值。
"""
a=int(input("请输入数字a"))
b=int(input("请输入数字b"))
c=int((a**b)/b)
print(c)
"""
#4.输入一个字符串，用一条语句将其输出顺序进行调换。
"""
a=input("请输入一个字符串")
print(a[::-1])
"""
#5.输入一个字符串，输出其长度。
#len(string)
#返回字符串长度
#count(str, beg= 0,end=len(string))
#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出
#现的次数
#split(str="", num=string.count(str))
#num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取
#num 个子字符串
#isdigit()
#如果字符串只包含数字则返回 True 否则返回 False
"""
a="gstraklsastrastdas"
print(a)
print("字符串长度为%d"%(len(a)))
b="st"
print("st在2-17位出现的次数为：%d"%(a.count(b,2,17)))
print(a.split('st',2))
print(a.isdigit())
"""

#6.输入一个字符串‘abcdabkrajb’，分别求出‘ab’出现的次数和‘e’出现的次数。
"""
s="abcdabkrajb"
print(s.count("ab"))
print(s.count("e"))
"""

#7.直接定义一个字符串'adc kdn lad',分别打印出以d分割的字符串的第二部分和第三部分。
"""
a="adckdnlad"
print(a.split("d"))
"""
#8.任意定义一个字符串,截取其第3到第5个字符，判断其中是否只包含数字，输出true
#和false，然后将其和‘hello’字符串连接起来打印输出。
"""
a="aslkdsancalsdijas"
print(a.isdigit())
print((a[2:4])+"hello")
"""

#9.创建一个包含字符串和数字的列表，打印出第3到5个元素，倒数第3个元素。
"""
a=["a","s","d","j","a","s",1,2,3,4,5]
print(a)
print(a[2:5])
print(a[-3])
"""
#10.创建一个列表，将第3个元素更改为‘third’，输出整个列表。
"""
a=["a","s","d","j","a","s",1,2,3,4,5]
print(a)
a[2]="third"
print(a)
"""
#11.创建两个列表，将其连接后，打印出第倒数第3和倒数第2两个元素，并将其与
#一个新的列表相加后输出。
"""
a=[1,2,3,4,5,6]
b=["a","b","c","d","e","f"]
print(a)
print(b)
c=a+b
print(a+b)
print(c)
"""

#12.创建一个列表，内部嵌套了3个列表
#a=['xiaoming','student',10],
#b=['xiaohong','coder',23],
#c=['xiaohuang','boss',35]，
#打印第2个列表的第1个元素，打印第3个列表的所有数据，删除第2个列表，打印
#整个大列表数据
"""
a=['xiaoming','student',10]
b=['xiaohong','coder',23]
c=['xiaohuang','boss',35]
lis=[a,b,c]
print(lis)
print(lis[1][0])
del lis[1]
print(lis)
"""
#13.将第12题中的大列表的末尾添加一个元素10。
#a) 将添加的元素通过列表打印出来。
#b）输出大列表中出现10这个元素的次数。
#c）输出第1个子列表中出现第一个元素‘10’的位置。
#d）对此列表进行反序输出。
#e）移除第2个子列表中的第3个元素，输出整个列表。
#f）移除整个列表中所有出现‘10’的元素并输出。
"""
a=['xiaoming','student',10]
b=['xiaohong','coder',23]
c=['xiaohuang','boss',35]
lis=[a,b,c]
print(lis)
#a
lis.append(10)
print(lis)

#b
print(lis.count(10))

#c***********
print(lis.index(10))

#d
lis.reverse()
print(lis)

#e
#del lis[1][2]
#print(lis)

#f
lis.remove(10)

print(lis)
"""















