from appium import webdriver

from time import sleep

# server 启动参数
desired_caps = {}
# 设备信息
# 平台的名称
desired_caps['platformName'] = 'Android'
# 系统的版本号
desired_caps['platformVersion'] = '5.1'
# 内容随便写但是不能是空字符串
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
# 需要打开的程序 包名
desired_caps['appPackage'] = 'com.android.settings'
# 需要打开的网页 启动名
desired_caps['appActivity'] = '.Settings'

# 解决输入中文问题 也可以不写
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 以上是前置代码，一个也不能少

#  单个元素定位  进入设置页面 ,通过ID定位方式点击搜索按钮, 通过class方式点击输入框返回按钮
# driver.find_element_by_id("com.android.settings:id/search").click()
# driver.find_element_by_class_name("android.widget.ImageButton").click()
# sleep(2)
# xpath 定位 点击显示
# driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
# xpath 定位 其他方式 也可以是id,class的形式
# driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.settings:id/title')]").click()
# driver.find_element_by_xpath("//*[contains(@class,'android.widget.TextView')]").click()

# 定位一组元素
# 进入设置页面 点击WLAN菜单栏(id定位对象列表中第1个) id 方式
# eles = driver.find_elements_by_id("com.android.settings:id/title")
# 点击WLAN菜单栏(class定位对象列表中第3个)
# eles=driver.find_elements_by_class_name("android.widget.TextView")
# 点击WLAN菜单栏(xpass定位对象列表中第3个)
eles = driver.find_elements_by_xpath("//*[contains(@class,'android.widget.TextView')]")

# print(type(eles),eles)
print(eles[3])
eles[3].click()

sleep(3)
driver.quit()
