import pandas as pd 
import json
import insights as ins
dfProducts = pd.read_csv('products.psv', sep='|', nrows=100000)
dateParser = lambda date: pd.to_datetime(date,unit='ms', errors='ignore')
dfInteractions = pd.read_csv('interactions.psv',sep="|",nrows=200000, parse_dates=['at'], date_parser=dateParser)
dfAll = dfInteractions.merge(dfProducts, on='pid')



	
# print(ins.product_main(dfAll, 'e99aa42d-dc18-44e1-9eca-932200a5c932', '2016-03-17', '2016-03-18'))

# print(ins.brand_main(dfAll, 'matrix', '2016-03-17', '2016-03-18'))

# print(ins.department_main(dfAll, 'AR', '2016-03-17', '2016-03-18'))
# ins.department_main(dfAll, 'AR')


print(ins.channel_main(dfAll, 'magazine_ecomm', '2016-03-17', '2016-03-18'))
# ins.channel_main(dfAll, 'magazine_ecomm')
