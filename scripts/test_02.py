import pytest
import allure

class Test_allure:
    def setup(self):
        print("test")
        pass

    def teardown(self):
        pass

    @allure.step(title="登录的测试脚本")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_login(self):
        allure.attach('输入用户名', '输入用户名的描述')
        print("输入用户名")
        allure.attach("输入密码","输入密码的描述")
        print("输入密码")
        allure.attach("登录", "登录的描述")
        print("登录")

        assert 1
     
    @allure.step(title="注册的测试脚本")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_zhuce(self):
        allure.attach('输入用户名', '输入用户名的描述')
        print("输入用户名")
        allure.attach("输入密码","输入密码的描述")
        print("输入密码")
        allure.attach("注册", "注册的描述")
        print("注册")

        assert 0

    # @pytest.mark.parametrize("a", [1, 2, 3])
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @allure.step('我是测试步骤001')
    # def test_al(self, a):
    #     allure.attach('描述', '我是测试步骤001的描述～～～')
    #     assert a != 2
