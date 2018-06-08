import sys

def fact(n):
    """
    阶乘函数
    :param n: 
    :return: 
    """

    if n == 0:
        return 1
    return  n * fact(n-1)

def div(n):
    """
    除法
    :param n: 
    :return: 
    """
    res = 10 / n
    return res

def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))


