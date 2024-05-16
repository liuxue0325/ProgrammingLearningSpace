# 使用for循环计算1+2+3+...+N的值。
N=int(input("请输入N的值："))#提示输入N的值
accN=0#给N的累加值赋初始值

for i in range(1,N+1):#for循环i为循环变量，1到N+1为循环范围
    accN=accN+i

print("从1加到%d的累加值为%d"%(N,accN))#打印累加结果