from appium import webdriver

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
# 滑动没有持续时间
#driver.swipe(188,659,148,248)
# 滑动持续5秒的时间
#driver.swipe(188,659,148,248,5000)

# 定位到存储菜单栏
el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位到WLAN菜单栏
el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 执行滑动操作
#driver.scroll(el1,el2)

# 模拟手指将存储菜单 滑动到 WLAN菜单栏位置
driver.drag_and_drop(el1,el2)
sleep(2)
driver.quit()