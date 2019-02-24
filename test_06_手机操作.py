from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from time import sleep

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 获取当前手机时间
print(driver.device_time)
# 获取手机的宽高
print(driver.get_window_size())
# 发送键到设备，home键 3，音量键加24，音量减25，返回键4
# driver.keyevent(24)
# sleep(2)
# driver.keyevent(25)
# sleep(2)
# driver.keyevent(4)
# sleep(2)
# driver.keyevent(3)

# 打开手机通知栏
# driver.open_notifications()
# 设置手机连接的网络
# driver.set_network_connection(1)
# driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
# 获取手机当前连接的网络
# print(driver.network_connection)
# 手机截图 ./ 当前目录
driver.get_screenshot_as_file("./xxx.png")

sleep(3)
driver.quit()