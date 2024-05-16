"""
有两个班的同学，班里同学们的名字可以使用字符串表示，
如何编写python程序找出在班级2中出现但没有在班级1中出现的学生的名字。
班级1名单：Joan Bill Niki Mark Mark
班级2名单：Tom Linda Bill
"""

num1=int(input('输入班级1中的人数：'))

class1=set()
for i in range(0,num1):
    name=input('输入班级1中同学%d的名字:'%(i+1))
    class1.add(name)

num2=int(input('输入班级2中的人数：'))

class2=set()
for i in range(0,num2):
    name=input('输入班级2中同学%d的名字:'%(i+1))
    class2.add(name)

different=class2-class1

print('打印班级2独有的学生的名字：')
for name in different:
    print(name)