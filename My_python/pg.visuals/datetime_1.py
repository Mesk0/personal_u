from datetime import datetime
# strptime含有两个实参，第一个实参传递一个表示时期的字符串，第二个实参设置日期的格式
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
print(first_date)
