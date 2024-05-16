"""
有两个班的同学，班里同学们的名字可以使用字符串表示，
如何编写python程序找出两个班名字相同的同学。
班级1名单：Joan Bill Niki Mark Mark
班级2名单：Tom Linda Bill
"""

'''
# 方法一：使用双重循环比较实现
#设置class1和class2两个列表
class1=['Joan','Bill','Niki','Mark','Mark']
class2=['Tom','Linda','Bill']

#循环遍历class1，其中每个元素都与class2中的元素做比较
for name1 in class1:
    # print('name1:%s'%name1)
    for name2 in class2:
        # print('name2:%s'%name2)
        if name1 == name2:#如果相同
            print(name1)#将该元素打印出来

'''


"""
python中的集合：
集合是一个无序的集，用来保存不重复的元素，集合元素用逗号分隔，用打括号括起来。
集合中存储的基本的且不可变的数据类型，如整型、浮点型、字符串、元组等;
不能存储可变数据类型，如列表、字典、集合。
集合的创建格式
    创建空集合： a=set()
    创建非空集合： b={1,2,'abc'}
可以将字符串、列表、元组、字典转换为集合，字典在转换后只保留key;
a='abcd'
test=set(a)
print(test)

b=[1,2,3]
test=set(b)
print(test)

c=(1,2,'abc')
test=set(c)
print(test)

d={'a':1,'b':2,'c':3}
test=set(d)
print(test)

因为集合是无序的，所以不能通过索引的方式访问，可以使用遍历访问。
可以使用add(),添加集合中的元素，使用remove()，移除集合中的元素。
 nums={1,2,3}
 nums.add(6)
 nums.remove(1)
 print(nums)
"""

"""
集合运算：
    交集：取两个集合公共的元素 （&/intersection）
    并集：取两集合的全部元素   （|/union）
    差集：取一个集合中另一个集合没有的元素 （-/differenc）
a={1,2,3,4}
b={3,4,5,6}

print(a&b)
print(a.intersection(b))

print(b&a)
print(b.intersection(a))

print(a|b)
print(a.union(b))

print(b|a)
print(b.union(a))

print(a-b)
print(a.difference(b))

print(b-a)
print(b.difference(a))
"""

# 方法二：使用集合求解

#输入班级1的学生数量，存储至num1
num1=int(input('输入班级1的学生数量：'))

class1=set()#初始化集合class1
#通过循环，输入班级1学生的姓名
for i in range(0,num1):
    name=input('输入学生%d的姓名：'%(i+1))
    class1.add(name)#添加至集合class1

#输入班级1的学生数量，存储至num1
num2=int(input('输入班级1的学生数量：'))

class2=set()#初始化集合class2
#通过循环，输入班级2学生的姓名
for i in range(0,num2):
    name=input('输入学生%d的姓名：'%(i+1))
    class2.add(name)#添加至集合class2

#通过取交集找出class1与class2重名的学生，存储至same
same=class1 & class2
print("重名的学生：")
for name in same:
    print(name)#打印重名学生的名字