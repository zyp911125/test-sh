# 函数的执行顺序
import pytest
class TestABC:
    def test_01(self):
        print("5")
    def test_02(self):
        print("4")
    @pytest.mark.run(order=2)
    def test_03(self):
        print("3")

    def test_04(self):
        print("2")
    @pytest.mark.run(order=1)
    def test_05(self):
        print("1")
# 0>较小的正数>较大的正数>无标记>较小的负数>较大的负数