import urllib.request
import urllib.parse
import func
import time


get_baidu_qianxi_data_func = func.getBaiduQianxi()
area_choice = "area_choice"
while not area_choice.isnumeric():
    area_choice = input("1.成都 2.海口 3.自定义")
scale_choice = "scale_choice"
while not scale_choice.isnumeric():
    scale_choice = input("请输入迁入迁出排名单位\n1.省级 2.市级：")
direction_choice = "direction_choice"
while not direction_choice.isnumeric():
    direction_choice = input("1.迁入来源地 2.迁出目的地")
date_choice = "date_choice"
while not date_choice.isnumeric():
    date_choice = input("1.2022春运 2.2021国庆 3.2021春运 4.2020国庆 5.2020春运 6.自定义")
base_url = get_baidu_qianxi_data_func.process_scale_choice(scale_choice=scale_choice)
date_se_list = get_baidu_qianxi_data_func.process_date_choice(date_choice=date_choice)
date_list = get_baidu_qianxi_data_func.generate_date_list(date_se_list)
dir_name = get_baidu_qianxi_data_func.create_directory(area_choice, date_choice, direction_choice, scale_choice)
for date in date_list:
    request = get_baidu_qianxi_data_func.init_request(scale_choice, date, direction_choice, area_choice)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    content = content.split("(")[1].split(")")[0]
    file = open("./%s/%s.json" % (dir_name, date), mode="w")
    file.write(content)
    file.close()
    print("%s.json写入完毕" % date)
    get_baidu_qianxi_data_func.create_xlsx("./%s/%s.json" % (dir_name, date), date, scale_choice)
    time.sleep(5)
print("结束")