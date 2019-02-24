from appium import webdriver

from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
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

# 通过ID定位方式点击搜索按钮  超时时间为10s，每隔1秒搜索一次元素是否存在，如果元素存在返回定位对象并退出
search_button=WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id("com.android.settings:id/search"))
search_button.click()

driver.quit()