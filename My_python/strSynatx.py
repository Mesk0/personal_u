"""string替换
基本结构：'string=%s'%args
"""

string = "good"     #类型为字符串
string1 = "enough"
print("string=%s" %string)
# 输出的打印结果为 string=good

print("string=%3s" %string) 
# 输出的打印结果为 string=good(数字3的意思是：字符串的长度为3。当字符串的长度大于3时，按照字符串的长度打印出结果)

print("string=%+6s" %string)
# 输出的打印结果为 string=  good(当字符串的长度小于6时，在字符串的左侧填补空格，使得字符串的长度为6)

print("string=%-6s" %string)  
# 输出的打印结果为 string=good  (当字符串的长度小于6时，在字符串的右侧填补空格，使得字符串的长度为6)
#小数点后的数字表示截取的字符串长度

print("string=%.3s" %string)  
# 输出的打印结果为 string=goo(%.3s的意思是：截取字符串的前3个字符，当截取字符串的字符长度大于字符串时，输出的结果是整个字符串)

print("string=%a.bs" %string)  
# 输出的打印结果为 string='good'.bs，先是根据小数点后面的数字b截取字符串，当截取的字符串长度小于a时，需要在字符串的左侧填补空格，使得字符串的长度变为a

print("string=%*.*s" %(6, 3, string))  
# 输出的打印结果为 string=   goo，%*.*s表示精度， 两个*的值分别由%string前面被两个逗号隔开的数值来指定

print("string1=%s,string2=%s"%(string, string1))
# 多个需要替换，需要用到元组。