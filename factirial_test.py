import unittest

from factirial import fact, div

class TestFactirial(unittest.TestCase):
    """
    基本测试类
    """
    def test_fact(self):
        """
        任何以'test_'开头的方法都是测试用例
        :return: 
        """
        res = fact(5)
        self.assertEqual(res, 120)

    def test_error(self):
        """
        测试由运行错误引发的异常
        :return: 
        """
        self.assertRaises(ZeroDivisionError, div, 0)

if __name__ == '__main__':
    unittest.main()
