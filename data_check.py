class DataCheck:

    def __init__(self, action_data_dict, result_dict, data, action_data_key):

        if action_data_dict == result_dict:
            print('source_visit_id：{}\t，visit_id：{}\t前端数据流同步服务保存所有接口返回的actions信息与数据库查询一致'
                  .format(data[0], action_data_key))
        else:
            print('source_visit_id：{}\t，visit_id：{}\t前端数据流同步服务保存所有接口返回的actions信息与数据库查询不一致'
                  .format(data[0], action_data_key))
