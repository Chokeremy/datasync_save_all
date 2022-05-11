
# 请求保存所有数据的接口url
URL = 'http://synyi-cdss-datasync-1701-test.sy/api/datasync/Patient'

# 请求保存所有数据的接口的请求头headers
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/101.0.4951.41 Safari/537.36['}

# 请求保存所有数据的接口的入参
JSON_PARAMS = '{"visit_info":{"source_visit_id":"%s","source_patient_id":"","source_app":"cds_sync","dept_name":"骨科",' \
              '"dept_code":"123","visit_time":"2020-01-01 18:00:00","visit_state_name":"结束","visit_type":"I",' \
              '"in_dept_name":"骨科","in_ward_name":"骨科","in_time":"2022-05-10T11:37:32.311Z","out_dept_name":"骨科",' \
              '"out_ward_name":"","out_time":"2022-05-10T11:37:32.311Z","source_org_code":"PT1","is_valid":true,' \
              '"sex_name":"男","bed_name":"02","source_inpat_no":"0050F70897","bed_doc_id":"string",' \
              '"bed_doc_name":"string"},"is_synchronous":true} '

# 数据库连接信息
DBNAME_HDR = 'hdr_cdss_test'
DBNAME_CDS = 'cdss_test'
USER = 'gongqiaoshu'
PASSWORD = '123456'
HOST = '172.16.0.20'
PORT = 5432

# 数据库查询sql
SQL_PARAMS = 'select source_visit_id, visit_id from visit.visit_record where dept_id = 62 and out_time is not null;'
SQL_RESULT = 'select visit_id, action_id from cdss.action_run_result where perform_id in (select perform_id from (' \
             'select row_number() over (partition by visit_id order by create_time desc ) as row, ' \
             '* from cdss.action_run_result where visit_id = {}) as t where t.row = 1); '

# 打印*花
N = '*' * 100
