import tushare as ts

df = ts.get_stock_basics()
#data = ts.get_h_data('399001', index=True) #深证成指
#data = ts.get_h_data('399006', index=True) #创业板指
data = ts.get_h_data('000001', index=True) #沪指
print(data)
