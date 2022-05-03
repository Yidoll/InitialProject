"""
1. input
- 当程序执行到input，等待用户输入，输入完成之后才继续向下执行。
- 在python中，input接受到用户的输入后，一般存储到变量，方便使用。
- 在python中，input会把接收到的任意用户输入的数据都当作字符串处理。
"""

password = input('请输入您的密码： ')
print(f'您输入的密码是{password}')

# 查看数据类型
print(type(password))