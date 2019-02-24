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
# 解决输入中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 点击搜索按钮
#driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输入abc 再试一下中文
#input_str=driver.find_element_by_id("android:id/search_src_text")
#input_str.send_keys("中文")
#sleep(2)
#input_str.clear()

#获取所有元素class属性为“android.widget.TextView”的文本内容
# text_value=driver.find_elements_by_class_name("android.widget.TextView")
# for i in text_value:
#     print(i.text)

# 获取搜索按钮的属性
get_value = driver.find_element_by_id("com.android.settings:id/search")
print(get_value.get_attribute("name")) # content-desc 或者text的属性值(text没有时，是content-desc的值)
print(get_value.get_attribute("text"))
print(get_value.get_attribute("className"))
print(get_value.get_attribute("resourceId"))

# 定位到搜索按钮
get_value1 = driver.find_element_by_id("com.android.settings:id/search")
# 打印搜索按钮在屏幕上的坐标
print(get_value1.location)
#  获取包名和启动名
print(driver.current_package)
print(driver.current_activity)

driver.quit()


