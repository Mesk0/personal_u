import time, sys
indent = 0
indentIncreasing = True


try:
    while True:
        # 确保输出空格之后不会换行，end=''在第一个print()中调用
        # 字符串可以乘以int值，实现重复int值的次数
        print(' ' * indent, end='')
        print('********')
        # unknowed
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

# 输入ctrl+c触发此事件
except KeyboardInterrupt:
    sys.exit()