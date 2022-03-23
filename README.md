# BaiduHuiyan_Qianxi
示例url：https://huiyan.baidu.com/migration/cityrank.jsonp?dt=province&id=500000&type=move_in&date=20220321

百度慧眼 迁徙数据 Crawling

可获取省级、市级的迁入、迁出的json数据并自动保存为xlsx文件，支持的时间段为“2022春运、2021国庆”、“2021春运”、“2020国庆”、“2020春运以及自定义时间段”。

支持成都、海口和自定义查询，使用自定义查询之前需要找到其所对应的area_code，area_code对应的是示例url里的id

需要pandas、urllib、openpyxl

每获某一天的数据要暂停5秒
