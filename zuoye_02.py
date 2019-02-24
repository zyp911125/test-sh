from appium.webdriver.common.touch_action import TouchAction

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
desired_caps['appActivity'] = '.ChooseLockPattern'  # 根据ADB命令重新获取包名和启动名，还是设置所以包名不变，来到绘制图案的页面

# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 绘制图案锁
#  代码太长的解决方法1
# TouchAction(driver)\
#     .press(x=231,y=842)\
#     .move_to(x=480,y=0)\
#     .move_to(x=480,y=0)\
#     .move_to(x=0,y=480)\
#     .move_to(x=-480,y=480)\
#     .release()\
#     .perform()
#  方法2
# (TouchAction(driver)
#      .press(x=240,y=848) #(724,849)(1204,847)(1204.1329)(721,1329)(721,1807)
#      .move_to(x=484,y=0)
#      .move_to(x=480,y=0)
#      .move_to(x=0,y=480)
#      .move_to(x=-483,y=0)
#      .move_to(x=0,y=478)
#      .release()
#      .perform())

(TouchAction(driver)
    .press(x=231,y=842)
    .move_to(x=724,y=849)
    .move_to(x=1204,y=847)
    .move_to(x=1204,y=1329)
    .move_to(x=721,y=1329)
    .move_to(x=721,y=1807)
     .release()
     .perform())

sleep(2)
driver.quit()