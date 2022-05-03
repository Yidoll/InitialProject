"""
数据类型转换

"""
num = 1
print(num)
print(type(num))

# 1. 转换整数
newNum = int(num)
print(newNum)
print(type(newNum))

# 2. 转换成浮点
floatNum = float(num)
print(floatNum)
print(type(floatNum))

# 3. str() -- 将数据转换成字符串
num1 = 100
str1 = str(num1)
print(str1)
print(type(str1))

# 4. tuple
list1 = [10, 20, 30]
print(tuple(list1))

# 5. list()
t1 = (100, 200, 300)
print(list(t1))

# 6. eval() --用来计算在字符串中的有效python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000,2000, 3000)'
str5 = '[1000, 2000, 3000]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
