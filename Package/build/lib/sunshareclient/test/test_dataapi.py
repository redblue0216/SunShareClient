
from sunshareclient.client.api import DataAPI



### 设置除了token_key和token外，额外的参数
tmp_dict = {}
tmp_dict['entity'] = 'XJJX'
tmp_dict['start_time'] = '2022-05-30,00:00:00'
tmp_dict['end_time'] = '2022-06-01,00:00:00'
sunshareclient = DataAPI(token_key = 7890,
                    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODM1MzUyODIuMDA5NzE2NSwidXNlciI6InRlc3QifQ.gwhPIB_m4nAFGfIdSSdircknCQxQ82leyw8ylsTcdHs',
                    timeout=6000)
# df = sunshareclient.query(dataapi='get_wind_nwp_data_updated_local',params=tmp_dict)
df = sunshareclient.get_wind_nwp_data_updated_local(params=tmp_dict)
# df = sunshareclient.get_wind_nwp_data_history_local(params=tmp_dict)
# df = sunshareclient.get_wind_measure_data_local(params=tmp_dict)
# df = sunshareclient.get_wind_turbine_data_local(params=tmp_dict)
print(df)


