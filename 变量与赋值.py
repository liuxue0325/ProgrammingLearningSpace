# 命名规则：
# 只能由A-Z a-z _ 0-9组成，第一个字符不能是数字。
# 不能与python语言本身使用的名称相同，python保留字。
glass1 = input("请输入杯子1中的饮料：")#根据提示，输入杯子1中的饮料
glass2 = input("请输入杯子2中的饮料：")#根据提示，输入杯子2中的饮料
temp = ""#临时杯是一个空杯子

print("交换前杯子1何和杯子2中的饮料为：")#打印交换前，杯子1和杯子2中的饮料
print(glass1)
print(glass2)

temp = glass1#将杯子1中的可乐倒入临时杯子
glass1 = glass2#将杯子2中的牛奶倒入杯子1
glass2 = temp#将临时杯子中的可乐倒入杯子2

print("交换后杯子1和杯子2中的饮料为：")#打印交换后，杯子1和杯子2中的饮料
print(glass1)
print(glass2)
