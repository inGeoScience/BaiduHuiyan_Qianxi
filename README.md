# BaiduHuiyan_Qianxi
# 百度慧眼 迁徙数据 Crawling

# 介绍
该project可获取省级、市级的迁入、迁出的json数据并自动保存为xlsx文件，支持的时间段为“2022春运、2021国庆”、“2021春运”、“2020国庆”、“2020春运以及自定义时间段”。
支持成都、海口和自定义查询，使用自定义查询之前需要找到其所对应的area_code，area_code对应的是示例url里的id
需要pandas、urllib、openpyxl
每获某一天的数据要暂停5秒

# 使用
##### 第一步输入的参数决定查询的地区
##### 第二步输入的参数决定迁徙数据的单位级别（省、直辖市或地级市）
##### 第三步输入的参数决定获取的是迁入数据还是迁出数据
##### 第四步输入的参数决定查询日期
##### 若地区选择的自定义，则第五步需要输入该地区的代码

# 原理
##### 某省或直辖市以地级市为单位的迁徙数据示例url：https://huiyan.baidu.com/migration/cityrank.jsonp?dt=province&id=500000&type=move_in&date=20220321
##### 某省或直辖市以省、直辖市为单位的迁徙数据示例url：https://huiyan.baidu.com/migration/provincerank.jsonp?dt=province&id=500000&type=move_in&date=20220322
##### 某地级市以地级市为单位的迁徙数据示例url:https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=350100&type=move_in&date=20220322
##### 某地级市以省、直辖市为单位的迁徙数据示例url：https://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=440100&type=move_in&date=20220322
##### dt参数指所查询地区的等级，若为省或直辖市，则dt=province；若为地级市，则dt=city。在该project中dt由id倒数第三位数字来判定。若倒数第三位数字不为0，则dt=city；若为0，则dt=province。
##### 迁徙数据的单位级别由url的目录决定，若目录为/cityrank.jsonp，则数据单位级别为地级市；若目录为/provincerank.jsonp，则数据单位级别为省、直辖市。
##### id参数定义所查询的地区，如500000为重庆市，350100为福州市。
##### type参数定义数据为迁入数据还是迁出数据。
##### date参数定义查询日期。
