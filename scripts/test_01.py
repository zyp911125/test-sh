import random
import pytest
import allure
class TestLogin:
    def setup_class(self):
        print("setup---->")
    def teardown_class(self):
        print("teardown-->")
    # def test_01(self):
    #     print("测试01---->")allure generate report/ -o report/html --clean
    #     assert 1
    # 失败重试，用程序控制，可在成功后不继续往下重试
    # def test_02(self):
    #     num=random.randint(1,3)
    #     print(num)
    #     if num==1:
    #         print("测试02---->")
    #         assert 1
    #     else:
    #         assert 0 # 断言失败
    # 跳过函数
    # @pytest.mark.skipif(condition=2>1,reason="跳过该函数")
    # def test_b(self):
    #     print("测试哦----")

    #  标记为预期失败函数 分四种情况 注意：xfail 就是预期失败的意思
    # 预期成功，结果成功 Passed 绿色
    # @pytest.mark.xfail(False,reason="预期成功")
    # def test_01(self):
    #     print("测试01---->")
    #     assert 1
    # # 预期成功，结果失败 Failed 红色
    # @pytest.mark.xfail(False, reason="预期成功")
    # def test_02(self):
    #     print("测试02---->")
    #     assert 0
    # # 预期失败，结果失败 XFailed  橙色
    # @pytest.mark.xfail(True, reason="预期失败")
    # def test_03(self):
    #     print("测试03---->")
    #     assert 0
    # # 预期失败，结果成功 XPassed 红色
    # @pytest.mark.xfail(True, reason="预期失败")
    # def test_04(self):
    #     print("测试04---->")
    # assert 1
    # 函数数据参数化 单个参数，多个参数
    # @pytest.mark.parametrize("name",["zhangsan","lisi"]) # name 有两个取值，函数会运行两次
    # def test_01(self,name):
    #      print(name)
    #      assert 1
    # 多个值，按组打印zhangsan 18,lisi 20
    # @pytest.mark.parametrize(("name","age"), [("zhangsan","18"), ("lisi","20")])
    # def test_01(self, name,age):
    #     print(name)
    #     print(age)
    #     assert 1
    @pytest.mark.parametrize("a,b",[(3,6)])
    def test_02(self,a,b):
        print(a)
        print(b)
        assert 1

