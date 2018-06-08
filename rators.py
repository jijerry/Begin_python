"""
迭代器，生成器，装饰器
"""

# 迭代器

class Counter(object):

    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        # 返回下一个值直到当前值大于high
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# c = Counter(5, 10)
# for i in c:
#     print('you: {}', i)


# 运行细节
c = Counter(5, 10)
iterator = iter(c)

while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break



# 生成器

def my_generator():
    print("inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

for char in my_generator():
    print(char)

