#!/usr/bin/python
"""
编程胶囊：https://www.codejiaonang.com/
菜鸟教程：https://www.runoob.com/python/python-reg-expressions.html
"""
import re

line = "Cats are smarter than dogs"

# match 和 search 是匹配一次， findall 匹配所有。
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
# 删除非数字(-)的字符串
num1 = re.sub(r'\D', "", phone)


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
# ?P将分组命名
print(re.sub('(?P<value>\d+)', double, s))
import re

line = "Cats are smarter than dogs dogs";
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式，影响 ^ 和 $
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释
matchObj = re.search(r'dogs', line, re.M | re.I)
print(matchObj.group())

# 分组回溯，匹配相同标签
a = """<font>ziti</font>
<font>b-b</p>
<font1>zit2i</font1>
"""
print(re.findall(r"<\w+>.*?</\w+>", a))
print(re.findall(r"<(\w+)>(.*?)</\1>", a))

# 非捕获分组?:在该分组之后，无法引用该分组，因为该分组没有分组名，没有分组号，也不会占用分组编号；
print(re.findall(r"<\w+>(.*?)</\w+>", a))

# (?=.*?[a-z])(?=.*?[A-Z]).+ 这段正则表达式规定了匹配的字符串中必须包含至少一个大写和小写的字母。
