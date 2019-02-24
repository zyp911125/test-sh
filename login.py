import pytest

def test_login(self):
    print("正在登陆")
    assert 1
if __name__ == '__main__':

    #  pytest.main("-s login.py") 此方式过期了，还能用
    pytest.main(["-s","login.py"]) # 推荐此方式