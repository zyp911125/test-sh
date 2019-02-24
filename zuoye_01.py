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

while True:
    try:
        driver.find_element_by_xpath("//*[contains(@text,'关于手机')]").click()
        # 找到后跳出循环
        break
    except Exception:
        # 翻页
         driver.swipe(100,2000,100,1000,5000)
#  所有关于手机界面的 文本框
eles=driver.find_elements_by_class_name("android.widget.TextView")
for i in eles:
    if i.text=="5.1":
        print("有")
        break
else:
    print("没有")

sleep(2)
driver.quit()