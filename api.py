from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import Response
import pandas as pd 
import insights as ins
from datetime import datetime, timedelta


dfProducts = pd.read_csv('products.psv', sep='|', nrows=100000)
dateParser = lambda date: pd.to_datetime(date,unit='ms', errors='ignore')
dfInteractions = pd.read_csv('interactions.psv',sep="|",nrows=200000, parse_dates=['at'], date_parser=dateParser)
dfAll = dfInteractions.merge(dfProducts, on='pid')

def get_period(begin, end):
	if begin == None:
		begin = datetime.now()	
	else:
		begin = datetime.strptime(begin, "%Y-%m-%d")

	if end == None:
		end = begin + timedelta(days=1)
		end = end.strftime('%Y-%m-%d')
	
	begin = begin.strftime('%Y-%m-%d')
	return (begin, end)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/brand/<brand>")
def brand_handler(brand):
	begin = request.args.get('begin')
	end = request.args.get('end')
	
	if begin == None and end != None:
		abort(400, 'INVALID PARAMETERS')
	
	period = get_period(begin,end)  	
	return jsonify(ins.brand_main(dfAll, brand, period[0], period[1]))
	
@app.route("/product/<product>")
def product_handler(product):
	begin = request.args.get('begin')
	end = request.args.get('end')
	
	if begin == None and end != None:
		abort(400, 'Invalid Parameters')
	
	period = get_period(begin,end)  	
	return jsonify(ins.product_main(dfAll, product, period[0], period[1]))

@app.route("/department/<department>")
def department_handler(department):
	begin = request.args.get('begin')
	end = request.args.get('end')
	
	if begin == None and end != None:
		abort(400, 'Invalid Parameters')
	
	period = get_period(begin,end)  	
	return jsonify(ins.department_main(dfAll, department, period[0], period[1]))

@app.route("/channel/<channel>")
def channel_handler(channel):
	begin = request.args.get('begin')
	end = request.args.get('end')
	
	if begin == None and end != None:
		abort(400, 'Invalid Parameters')
	
	period = get_period(begin,end)  	
	return jsonify(ins.channel_main(dfAll, channel, period[0], period[1]))

if __name__ == "__main__":
    app.run()











