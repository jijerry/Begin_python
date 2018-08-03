'myfact module'

def factor(num):
    """
    返回给定数据的阶乘值
    :param num: 计算其阶乘的整数值
    :return: 阶乘值，如果传递参数为负数，则为-1
    """
    if num >= 0:
        if num ==0:
            return 1
        return num * factor(num-1)
    else:
        return -1
