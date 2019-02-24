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
desired_caps['appActivity'] = '.Settings'

# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# tap , press,release，wait,long_press, move_to

# 1.通过元素定位方式 敲击屏幕WLAN
# el=driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).tap(el).perform()
# 通过坐标方式敲击屏幕，WLAN坐标:x=155,y=250
# TouchAction(driver).tap(x=155,y=250).perform()

# 2.通过元素定位方式 按下离开操作
# TouchAction(driver).press(el).release().perform()
# 通过坐标方式按下屏幕，WLAN坐标:x=155,y=250
# TouchAction(driver).tap(x=155,y=250).release().perform()

# 3.点击WLAN选项 ,长按WiredSSID选项 5秒 ,然后松开
driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
el = driver.find_element_by_id("android:id/title")
# TouchAction(driver).press(el).wait(5000).release().perform()
# 坐标的方式
# TouchAction(driver).press(x=770,y=667).wait(5000).release().perform()
# 4.另外一种长按 long_press
# TouchAction(driver).long_press(el,duration=5000).release().perform()
# 通过坐标方式长按元素，WiredSSID坐标:x=770,y=667
TouchAction(driver).long_press(x=770, y=667, duration=5000).release().perform()

sleep(2)
driver.quit()
