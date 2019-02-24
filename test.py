import pytest

# 函数级别
# class Test_ABC:
#     def setup(self):
#         print("setup执行了")
#     def test_01(self):
#         print("测试01执行了")
#     def test_02(self):
#         print("测试02执行了")
#     def teardown(self):
#         print("teardown执行了")
#
# if __name__ == '__main__':
#     pytest.main("-s test.py")

# 类级别
class Test_ABC:
    def setup_class(self):
        print("setup执行了")
    def teardown_class(self):
        print("teardown执行了")
    def test_01(self):
        print("函数01执行了")
    def test_02(self):
        print("函数02执行了")

if __name__ == '__main__':
    pytest.main("-s test.py")