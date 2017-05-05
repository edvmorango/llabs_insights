# llabs_insights
A Flask Restful API provided by some insights.

This project has the objective to extract some insights from two PSV files(if i get authorization i will post the links here).

Requirements
Python 3.5

Setup

Open the terminal, go to the project directory and run:
```
sh setup.sh
```
The PSV file must be in the same directory as "insights.py"

To start the API you must run:
```
python api.py
```
if you are not using a ENV manager, try
```
python3.5 api.py
```
There are four endpoints:

/brand/<brand>
/product/<product>
/department/<department>
/channel/<channel>

And three valid queries:
```
/brand/<brand>
```
```
/brand/<brand>?begin=<date string(YYYY-MM-dd)>
```
```
/brand/<brand>?begin=<date string(YYYY-MM-dd)>&end=<date string(YYYY-MM-dd)>
```
The fields are:
Products:
```
actions : Show all actions, the count and percentage
brand : The product brand
category: The product category
channels: Show all channels, the count and percentage
channels_total: Channels count 
department: Show all departments
name: The product name
price_avg: The product average price
price_max: The product max price
price_min: The product min price
product_id: The product identifier
rating: The rating
revenue: Total sales
sells_per_price:Shows all the prices that the product had, the count and percentage
total_boughts: Number of bought products
total_dislikeds: Number of disliked products
total_likeds: Number of liked products
total_views: Number of views
unique_users: Total single users who interacted
```


