# //*contains(@text,’设’)包含
# //*[@text=’设’]精确查找 1
#   //*[@text=’设’ and contains(@text,’置’)] 多条件
# "text,设置，0" 0表示包含，1表示精确查找

def make_xpath_midle_feature(loc):
    # 拼接xpath中间的部分
    args = loc.split(",")
    feature = " "
    index0 = 0  # 为了代码规范，而定义的活变量
    index1 = 1
    index2 = 2
    if len(args) == 2:
        feature = "contains(@" + args[index0] + ",'" + args[index1] + "')" + "and"
    elif len(args) == 3:
        if args[index2] == "1":
            feature = "@" + args[index0] + "='" + args[index1] + "'" + "and"
        elif args[index2] == "0":
            feature = "contains(@" + args[index0] + ",'" + args[index1] + "')" + "and"
    return feature


def make_xpath_feature(loc):
    feature_start = "//*["
    feature_end = "]"
    feature = " "

    if isinstance(loc, str):  # loc 是字符串
        # 如果是正常的xpath
        if loc.startswith("//"):
            return loc
        feature = make_xpath_midle_feature(loc)
    else:
        # loc 是列表
        for i in loc:
            feature += make_xpath_midle_feature(i)
    feature = feature.rstrip("and")  # 去掉尾部的and
    loc = feature_start + feature + feature_end
    return loc


def main():
    # loc="text,设置,0"
    # loc=["text,设置","index,20,1","id,34"]
    loc = "//*contains(@text,’设’)"
    a = make_xpath_feature(loc)
    print(a)


if __name__ == '__main__':
    main()
