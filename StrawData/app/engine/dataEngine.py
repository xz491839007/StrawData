import time
import tushare as ts
import pandas
import app.utils.var as var

class dataEngine(object):
    """数据业务层代码，第一期主要的核心功能是通过tushare来获得基本面的信息"""
    now_time = time.time()
    pro = ts.set_token(var.TOKEN)
    pro = ts.pro_api(var.TOKEN)
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    def gets(self):
        print('----------------------')
        # 进行同步接口的处理，并且进行数据的同步和数据的处理
        df = self.pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
        print(df)



# 直接运行脚本可以进行测试
if __name__ == '__main__':
    data = dataEngine()
    data.gets()