from constant_config import *
from request_url import RequestUrl
from database_connect import DatabaseConnect
from data_check import DataCheck
import json


class StartRequest:

    def __init__(self):
        print('开始测试前端数据流同步服务保存所有接口返回的actions信息与数据库查询是否一致')

    @staticmethod
    def run():
        # 1.start_url 准备请求url，准备请求数据
        data_list = DatabaseConnect(DBNAME_HDR, USER, PASSWORD, HOST, PORT).get_data(SQL_PARAMS)
        # 2.发送url请求，获取响应，提取数据
        for data in data_list:
            # 入参json转化成字典
            dict_data = json.loads(JSON_PARAMS % data[0])
            # 调用接口请求响应
            json_str = RequestUrl(URL, HEADERS, dict_data).parse_url()
            # 提取响应数据组合成字典
            action_data_key = json.loads(json_str)['Data']['visit_id']
            action_data_list = set([i['action_id'] for i in json.loads(json_str)['Data']['actions']])
            action_data_dict = {action_data_key: action_data_list}
            print(N)
            if action_data_key != data[1]:
                print('接口执行查询的visit_id：{}和数据库查询的visit_id：{}不一致'.format(action_data_key, data[1]))
            print('接口返回的actions信息:', action_data_dict)
            # 3.数据库查询数据
            # 数据库查询sql加上visit_id
            sql_result = SQL_RESULT.format(action_data_key)
            result_list = DatabaseConnect(DBNAME_CDS, USER, PASSWORD, HOST, PORT).get_data(sql_result)
            # 查询数据库结果组合成字典
            result_value_list = set([i[1] for i in result_list])
            result_dict = {action_data_key: result_value_list}
            print('数据库查询的action信息:', result_dict)
            # 4.响应数据和数据库查询数据对比，判断对错
            DataCheck(action_data_dict, result_dict, data, action_data_key)


if __name__ == '__main__':
    start_request = StartRequest()
    start_request.run()
