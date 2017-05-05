import pandas as pd
import json
import ast
def perc(a,b):
	if b == 0:
		return 0

	p = a/b * 100 
	return round(p,2)




def product_main(df, pid, dt_begin, dt_end):
	product = df[ (df['pid'] == pid) & (df['at'] >= dt_begin) & (df['at'] < dt_end)]
	if int(product.size) == 0:
		return {}

	# Possible actions of interaction
	bought = product[product['action'] == 'bought']
	liked  = product[product['action'] == 'likeProduct']
	disliked = product[product['action'] == 'dislikeProduct'] 
	cart = product[product['action'] == 'addedtocart']
	view = product[product['action'] == 'viewed']

	# Total of interactions (if not specified, the size function will get the Data Frame total of elements)
	total_boughts = int(bought['action'].size)
	total_likeds = int(liked['action'].size)
	total_dislikeds = int(disliked['action'].size)
	total_incart = int(cart['action'].size)
	total_views =  int(view['action'].size)
	
	#Simple calculated Data
	revenue = round(bought['price_at'].sum(),2)
	rating = round(product['rating'].mean(),2)
	unique_users = product['uid'].unique().size

	total_liked_disliked_intercations = total_likeds + total_dislikeds
	liked_percentage = perc(total_likeds, total_liked_disliked_intercations)
	disliked_percentage = perc(total_dislikeds, total_liked_disliked_intercations)

	price_min = product["price_at"].min()
	price_avg = round(product["price_at"].mean(),2)
	price_max = product["price_at"].max()	

	# Grouped  data
	channels = product.groupby(['channel_id']).size().reset_index().rename(columns={0:'count'})
	channels_total = channels['count'].sum().item()
	channels['percentage'] = channels['count'].map(lambda x: perc(x,channels_total))
	
	actions = product.groupby(['action']).size().reset_index().rename(columns={0:'count'})
	actions_total = actions['count'].sum().item()
	actions['percentage'] = actions['count'].map(lambda x: perc(x,actions_total))
		
	sells = bought.groupby(['price_at']).size().reset_index().rename(columns={0:'count'})
	sells_total = sells['count'].sum()
	sells['percentage'] = sells['count'].map(lambda x: perc(x,sells_total))

	# Header 
	name = product.iloc[0]['name']
	brand = product.iloc[0]['brand']
	category = product.iloc[0]['category']
	department = product.iloc[0]['department']

	# Body
	body = { 'product_id' : pid,
			 'name' : name,
			 'brand' : brand,
			 'category' : category,
			 'department' : department,
			 'revenue' :  revenue,
			 'rating' : rating,
			 'price_min' : price_min,
			 'price_avg' : price_avg,
			 'price_max' : price_max,
			 'unique_users' : unique_users,
			 'total_views' : total_views,
			 'total_boughts' : total_boughts,
			 'total_likeds' : total_likeds,
			 'total_dislikeds' : total_dislikeds,
			 'actions' : ast.literal_eval(actions.to_json()),
			 'actions_total' : actions_total,
			 'channels' : ast.literal_eval(channels.to_json()),
			 'channels_total' : channels_total,
			 'sells_per_price' : ast.literal_eval(sells.to_json())
			 
			}
	json_data = json.dumps(body, indent=4, separators=(',', ' : '), sort_keys=True)
	return json.loads(json_data)


def brand_main(df, brand_name, dt_begin, dt_end):
	brand = df[(df['brand'] == brand_name) & (df['at'] >= dt_begin) & (df['at'] < dt_end)]

	if int(brand.size) ==  0:
		return {}
	
	# Possible actions
	bought = brand[brand['action'] == 'bought']
	liked  = brand[brand['action'] == 'likeProduct']
	disliked = brand[brand['action'] == 'dislikeProduct'] 
	cart = brand[brand['action'] == 'addedtocart']
	view = brand[brand['action'] == 'viewed']

	# Total of interactions
	total_boughts = int(bought['action'].size)
	total_likeds = int(liked['action'].size)
	total_dislikeds = int(disliked['action'].size)
	total_incart = int(cart['action'].size)

	# Simple data
	rating = round(brand['rating'].mean(),2)
	revenue = round(bought['price_at'].sum().item(),2)
	total_views = view['action'].count().item()
	unique_users = brand['uid'].unique().size

	price_min = brand["price_at"].min()
	price_avg = round(brand["price_at"].mean(),2)
	price_max = brand["price_at"].max()	

	total_liked_disliked_intercations = total_likeds + total_dislikeds
	liked_percentage = perc(total_likeds, total_liked_disliked_intercations)
	disliked_percentage = perc(total_dislikeds, total_liked_disliked_intercations)

	# Grouped data 
	departments = brand.groupby(['department']).size().reset_index().rename(columns={0:'count'})
	departments_total = departments['count'].sum().item()
	departments['percentage'] = departments['count'].map(lambda x: perc(x,departments_total))

	products = brand.groupby(['name']).size().reset_index().rename(columns={0:'count'})
	products_total = products['count'].sum().item()
	products['percentage'] = products['count'].map(lambda x: perc(x,products_total))

	categories = brand.groupby(['category']).size().reset_index().rename(columns={0:'count'})
	categories_total = categories['count'].sum().item()
	categories['percentage'] = categories['count'].map(lambda x: perc(x,categories_total))

	channels = brand.groupby(['channel_id']).size().reset_index().rename(columns={0:'count'})
	channels_total = channels['count'].sum().item()
	channels['percentage'] = channels['count'].map(lambda x: perc(x,channels_total))
	
	actions = brand.groupby(['action']).size().reset_index().rename(columns={0:'count'})
	actions_total = actions['count'].sum().item()
	actions['percentage'] = actions['count'].map(lambda x: perc(x,actions_total))

	# Body
	body = {
			 'brand' : brand_name,
			 'revenue' :  revenue,
			 'rating' : rating,
			 'price_min' : price_min,
			 'price_avg' : price_avg,
			 'price_max' : price_max,
			 'unique_users' : unique_users,
			 'total_views' : total_views,
			 'total_boughts' : total_boughts,
			 'total_likeds' : total_likeds,
			 'total_dislikeds' : total_dislikeds,
			 'departments' : ast.literal_eval(departments.to_json()),
			 'departments_total' : departments_total,
			 'products' : ast.literal_eval(products.to_json()),
			 'products_total' : products_total,
			 'categories' : ast.literal_eval(categories.to_json()),
			 'categories_total' : categories_total,
			 'actions' : ast.literal_eval(actions.to_json()),
			 'actions_total' : actions_total,
			 'channels' :ast.literal_eval(channels.to_json()),
			 'channels_total' : channels_total
			}
	

	json_data = json.dumps(body, indent=4, separators=(',', ' : '), sort_keys=True)
	return json.loads(json_data)

def department_main(df, department_name, dt_begin, dt_end):

	department = df[(df['department'] == department_name) & (df['at'] >= dt_begin) & (df['at'] < dt_end)]

	if int(department.size) ==  0:
		return {}

	# Possible actions
	bought = department[department['action'] == 'bought']
	liked  = department[department['action'] == 'likeProduct']
	disliked = department[department['action'] == 'dislikeProduct'] 
	cart = department[department['action'] == 'addedtocart']
	view = department[department['action'] == 'viewed']

	# Total of interactions
	total_boughts = int(bought['action'].size)
	total_likeds = int(liked['action'].size)
	total_dislikeds = int(disliked['action'].size)
	total_incart = int(cart['action'].size)

	# Simple data
	rating = round(department['rating'].mean(),2)
	revenue = round(bought['price_at'].sum().item(),2)
	total_views = view['action'].count().item()
	unique_users = department['uid'].unique().size

	price_min = department["price_at"].min()
	price_avg = round(department["price_at"].mean(),2)
	price_max = department["price_at"].max()	

	total_liked_disliked_intercations = total_likeds + total_dislikeds
	liked_percentage = perc(total_likeds, total_liked_disliked_intercations)
	disliked_percentage = perc(total_dislikeds, total_liked_disliked_intercations)

	# Grouped data 
	products = department.groupby(['name']).size().reset_index().rename(columns={0:'count'})
	products_total = products['count'].sum().item()
	products['percentage'] = products['count'].map(lambda x: perc(x,products_total))

	categories = department.groupby(['category']).size().reset_index().rename(columns={0:'count'})
	categories_total = categories['count'].sum().item()
	categories['percentage'] = categories['count'].map(lambda x: perc(x,categories_total))

	channels = department.groupby(['channel_id']).size().reset_index().rename(columns={0:'count'})
	channels_total = channels['count'].sum().item()
	channels['percentage'] = channels['count'].map(lambda x: perc(x,channels_total))
	
	actions = department.groupby(['action']).size().reset_index().rename(columns={0:'count'})
	actions_total = actions['count'].sum().item()
	actions['percentage'] = actions['count'].map(lambda x: perc(x,actions_total))

	# Body
	body = {
			 'department' : department_name,
			 'revenue' :  revenue,
			 'rating' : rating,
			 'price_min' : price_min,
			 'price_avg' : price_avg,
			 'price_max' : price_max,
			 'unique_users' : unique_users,
			 'total_views' : total_views,
			 'total_boughts' : total_boughts,
			 'total_likeds' : total_likeds,
			 'total_dislikeds' : total_dislikeds,
			 'products' : ast.literal_eval(products.to_json()),
			 'products_total' : products_total,
			 'categories' : ast.literal_eval(categories.to_json()),
			 'categories_total' : categories_total,
			 'actions' : ast.literal_eval(actions.to_json()),
			 'actions_total' : actions_total,
			 'channels' :ast.literal_eval(channels.to_json()),
			 'channels_total' : channels_total
			}
	

	json_data = json.dumps(body, indent=4, separators=(',', ' : '), sort_keys=True)
	print(json_data)
	return json.loads(json_data)

def channel_main(df, channel_id, dt_begin, dt_end):

	channel = df[(df['channel_id'] == channel_id) & (df['at'] >= dt_begin) & (df['at'] < dt_end)]

	if int(channel.size) ==  0:
		return {}

	# Possible actions
	bought = channel[channel['action'] == 'bought']
	liked  = channel[channel['action'] == 'likeProduct']
	disliked = channel[channel['action'] == 'dislikeProduct'] 
	cart = channel[channel['action'] == 'addedtocart']
	view = channel[channel['action'] == 'viewed']

	# Total of interactions
	total_boughts = int(bought['action'].size)
	total_likeds = int(liked['action'].size)
	total_dislikeds = int(disliked['action'].size)
	total_incart = int(cart['action'].size)

	# Simple data
	rating = round(channel['rating'].mean(),2)
	revenue = round(bought['price_at'].sum().item(),2)
	total_views = view['action'].count().item()
	unique_users = channel['uid'].unique().size

	price_min = channel["price_at"].min()
	price_avg = round(channel["price_at"].mean(),2)
	price_max = channel["price_at"].max()	

	total_liked_disliked_intercations = total_likeds + total_dislikeds
	liked_percentage = perc(total_likeds, total_liked_disliked_intercations)
	disliked_percentage = perc(total_dislikeds, total_liked_disliked_intercations)

	# Grouped data 
	
	products = channel.groupby(['name']).size().reset_index().rename(columns={0:'count'})
	products_total = products['count'].sum().item()
	products['percentage'] = products['count'].map(lambda x: perc(x,products_total))

	categories = channel.groupby(['category']).size().reset_index().rename(columns={0:'count'})
	categories_total = categories['count'].sum().item()
	categories['percentage'] = categories['count'].map(lambda x: perc(x,categories_total))

	actions = channel.groupby(['action']).size().reset_index().rename(columns={0:'count'})
	actions_total = actions['count'].sum().item()
	actions['percentage'] = actions['count'].map(lambda x: perc(x,actions_total))

	departments = channel.groupby(['department']).size().reset_index().rename(columns={0:'count'})
	departments_total = departments['count'].sum().item()
	departments['percentage'] = departments['count'].map(lambda x: perc(x,departments_total))

	# Body
	body = {
			 'channel_id' : channel_id,
			 'revenue' :  revenue,
			 'rating' : rating,
			 'price_min' : price_min,
			 'price_avg' : price_avg,
			 'price_max' : price_max,
			 'unique_users' : unique_users,
			 'total_views' : total_views,
			 'total_boughts' : total_boughts,
			 'total_likeds' : total_likeds,
			 'total_dislikeds' : total_dislikeds,
			 'products' : ast.literal_eval(products.to_json()),
			 'products_total' : products_total,
			 'categories' : ast.literal_eval(categories.to_json()),
			 'categories_total' : categories_total,
			 'actions' : ast.literal_eval(actions.to_json()),
			 'actions_total' : actions_total,
			 'departments' :ast.literal_eval(departments.to_json()),
			 'departments_total' : departments_total
			}
	

	json_data = json.dumps(body, indent=4, separators=(',', ' : '), sort_keys=True)
	print(json_data)
	return json.loads(json_data)



