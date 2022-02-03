import urllib.request
import urllib.parse
import pandas
import os
import time
import json
import jsonpath


def create_xlsx(json_path, date, scale_choice):
    json_object = json.load(open(json_path, encoding="utf-8"))
    scale_choice = int(scale_choice)
    if scale_choice == 1:
        province_list = jsonpath.jsonpath(json_object, "$.data.list[*].province_name")
        value_list = jsonpath.jsonpath(json_object, "$.data.list[*].value")
        if province_list and value_list:
            df = pandas.DataFrame({
                "Province_Name": province_list,
                "Proportion": value_list
            })
            df.to_excel("./%s/%s.xlsx" % (json_path.split("/")[1], date))
            print("%s.xlsx写入完成" % date)
        else:
            print("%s.xlsx写入失败，未读取到json数据" % date)

    elif scale_choice == 2:
        province_list = jsonpath.jsonpath(json_object, "$.data.list[*].province_name")
        city_list = jsonpath.jsonpath(json_object, "$.data.list[*].city_name")
        value_list = jsonpath.jsonpath(json_object, "$.data.list[*].value")
        if province_list and city_list and value_list:
            df = pandas.DataFrame({
                "Province_Name": province_list,
                "City_Name": city_list,
                "Proportion": value_list
            })
            df.to_excel("./%s/%s.xlsx" % (json_path.split("/")[1], date))
            print("%s.xlsx写入完成" % date)
        else:
            print("%s.xlsx写入失败，json数据内没有内容或未获取json数据" % date)


def process_scale_choice(scale_choice):
    base_url = ""
    scale_choice = int(scale_choice)
    if scale_choice == 1:
        base_url = "https://huiyan.baidu.com/migration/provincerank.jsonp?"
    else:
        base_url = "https://huiyan.baidu.com/migration/cityrank.jsonp?"
    return base_url


def process_date_choice(date_choice):
    tiny_list = []
    if int(date_choice) == 1:
        tiny_list = ["20220110", time.strftime("%Y%m%d", time.localtime(time.time()))]
    elif int(date_choice) == 2:
        tiny_list = ["20210913", "20220109"]
    elif int(date_choice) == 3:
        tiny_list = ["20210119", "20210308"]
    elif int(date_choice) == 4:
        tiny_list = ["20200922", "20210118"]
    elif int(date_choice) == 5:
        tiny_list = ["20200110", "20200315"]
    elif int(date_choice) == 6:
        tiny_list.append(input("请输入起始日期，格式：20210101"：))
        tiny_list.append(input("请输入终止日期，格式：20210101"：))
    return tiny_list


def process_direction_choice(direction_choice):
    direction_choice = int(direction_choice)
    direction_str = ""
    if direction_choice == 1:
        direction_str = "move_in"
    elif direction_choice == 2:
        direction_str = "move_out"
    return direction_str


def process_area_choice(area_choice):
    area_choice = int(area_choice)
    area_code = ""
    if area_choice == 1:
        area_code = "510100"
    elif area_choice == 2:
        area_code = "460100"
    return area_code


def generate_date_list(date_se_list:list):
    pandas_date_list = pandas.date_range(date_se_list[0], date_se_list[1], freq="1D")
    date_list = []
    for date in pandas_date_list:
        date_list.append(date.strftime("%Y%m%d"))
    return date_list


def create_directory(area_choice, date_choice, direction_choice, scale_choice):
    area_choice = int(area_choice)
    date_choice = int(date_choice)
    direction_choice = int(direction_choice)
    scale_choice = int(scale_choice)
    area = ""
    date_range = ""
    direction = ""
    scale = ""
    if area_choice == 1:
        area = "成都"
    elif area_choice == 2:
        area = "海口"

    if date_choice == 1:
        date_range = "2022春运"
    elif date_choice == 2:
        date_range = "2021国庆"
    elif date_choice == 3:
        date_range = "2021春运"
    elif date_choice == 4:
        date_range = "2020国庆"
    elif date_choice == 5:
        date_range = "2020春运"
    elif date_choice == 6:
        date_range = "自定义"

    if direction_choice == 1:
        direction = "迁入来源地"
    elif direction_choice == 2:
        direction = "迁出目的地"

    if scale_choice == 1:
        scale = "省级"
    elif scale_choice == 2:
        scale = "市级"

    dir_name = "%s_%s_%s_%s" % (area, date_range, scale, direction)
    dir_exists = os.path.exists(dir_name)
    if dir_exists:
        print("\"" + dir_name + "\"" + "目录已存在，将覆盖目录里同名文件")
    else:
        os.mkdir(dir_name)

    return dir_name


def init_request(scale_choice, date, direction_choice, area_choice):
    base_url = process_scale_choice(scale_choice=scale_choice)
    direction = process_direction_choice(direction_choice)
    area_code = process_area_choice(area_choice)
    para = {
        # 如果主体为省，则需要改dt
        "dt": "city",
        "id": area_code,
        "type": direction,
        "date": date
    }
    url = base_url + urllib.parse.urlencode(para)
    my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/97.0.4692.71 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=my_headers)
    return request
