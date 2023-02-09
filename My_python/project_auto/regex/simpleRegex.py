import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# re.compile方法创建一个regex对象
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   # 添加括号，对表达式分组
mo = phoneNumRegex.search('My number is 415-555-4242')  # search方法创建一个match对象

# group方法显示match对象
print('phone number found: ' + mo.group())
# 向group()传递1、2取得不同分组匹配对象；或传入0和不传入参数，返回整个文本。
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))

# groups方法同时获取所有分组匹配对象
print(mo.groups())
areaCode, mainNumber = mo.groups()  # groups可用于多重赋值
print(areaCode)
print(mainNumber)

# 正则表达式搜索括号,在括号前加\对其进行字符转义
phoneNumRegex1 = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search('My number is (415)555-4242')
print(mo1.group(1))
print(mo1.group(2))

# |即管道，用于匹配许多表达式中的一个，第一次出现的匹配文本作为match对象返回。
heroRegex = re.compile(r'Batman|Tina Fey')
mo2 = heroRegex.search('Batman and Tina Fey.')
print(mo2.group())
mo3 = heroRegex.search('Tina Fey and Batman.')
print(mo3.group())

# |用于匹配多个模式中的一个，作为正则表达式的一部分
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')    # 案例：省略前缀
mo4 = batRegex.search('Batmobile lost a wheel')
print(mo4.group())
# 只返回了括号里匹配的对象
print(mo4.group(1))

# ?用于实现可选匹配，?的对象在匹配对象中出现一次或零次。
phoneRegex2 = re.compile(r'Bat(wo)?man')
mo5 = phoneRegex2.search('The adventure of Batman')
print(mo5.group())

mo6 = phoneRegex2.search('The adventure of Batwoman')
print(mo6.group())

# *意味着匹配零次或多次.
BatRegex2 = re.compile(r'Bat(wo)*man')
mo7 = BatRegex2.search('The adventure of Batman')
mo8 = BatRegex2.search('The adventure of Batwowowoman')
print(mo7.group())
print(mo8.group())

# +意味着匹配一次或多次
BatRegex3 = re.compile(r'Bat(wo)+man')
mo9 = BatRegex3.search('The adventure of Batman')
# print(mo9.group()) mo9 is None

mo10 = BatRegex3.search('The adventure of Batwowowowoman')
print(mo10.group())


# {}实现表示特定匹配次数。
haRegex = re.compile(r'(ha){3}')
haRegex1 = re.compile(r'(ha){2,}')
haRegex2 = re.compile(r'(ha){,3}')
mo11 = haRegex.search('hahaha')
mo12 = haRegex1.search('hahahahahahaha')
mo13 = haRegex2.search('ha')
print(mo11.group())
print(mo12.group())
print(mo13.group())


# ?应用在{}实现非贪心匹配
greedyHaRegex = re.compile(r'(ha){3,5}')
mo14 = greedyHaRegex.search('hahahahaha')
print(mo14.group())

nongreedyHaRegex = re.compile(r'(ha){3,5}?')
mo15 = nongreedyHaRegex.search('hahahahahahaha')
print(mo15.group())


#