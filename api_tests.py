import unittest
import api
from flask import json


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status, "200 OK" )

    def test_brand_none(self):
    	response =  self.app.get('/brand/x')
    	self.assertEqual(response.status, "200 OK" )

    def test_brand_full_param(self):
    	response =  self.app.get('/brand/matrix?begin=2016-03-17&end=2016-03-18')
    	
    	self.assertEqual(response.status, "200 OK")

    def test_brand_half_param(self):
    	response =  self.app.get('/brand/matrix?begin=2016-03-17')
    	self.assertEqual(response.status, "200 OK" )
 
    def test_brand_none_param(self):
    	response =  self.app.get('/brand/matrix')
    	self.assertEqual(response.status, "200 OK" )

    def test_brand_invalid_param(self):
    	response =  self.app.get('/brand/matrix?end=2016-03-18')
    	self.assertEqual(response.status, "400 BAD REQUEST" )

    def test_product_none(self):
    	response =  self.app.get('/product/x')
    	self.assertEqual(response.status, "200 OK" )

    def test_product_full_param(self):
    	response =  self.app.get('/product/e99aa42d-dc18-44e1-9eca-932200a5c932?begin=2016-03-17&end=2016-03-18')
    	
    	self.assertEqual(response.status, "200 OK")

    def test_product_half_param(self):
    	response =  self.app.get('/product/e99aa42d-dc18-44e1-9eca-932200a5c932?begin=2016-03-17')
    	self.assertEqual(response.status, "200 OK" )
 
    def test_product_none_param(self):
    	response =  self.app.get('/product/e99aa42d-dc18-44e1-9eca-932200a5c932')
    	self.assertEqual(response.status, "200 OK" )

    def test_product_invalid_param(self):
    	response =  self.app.get('/product/e99aa42d-dc18-44e1-9eca-932200a5c932?end=2016-03-18')
    	self.assertEqual(response.status, "400 BAD REQUEST" )

    def test_channel_none(self):
    	response =  self.app.get('/channel/x')
    	self.assertEqual(response.status, "200 OK" )

    def test_channel_full_param(self):
    	response =  self.app.get('/channel/magazine_ecomm?begin=2016-03-17&end=2016-03-18')
    	
    	self.assertEqual(response.status, "200 OK")

    def test_channel_half_param(self):
    	response =  self.app.get('/channel/magazine_ecomm?begin=2016-03-17')
    	self.assertEqual(response.status, "200 OK" )
 
    def test_channel_none_param(self):
    	response =  self.app.get('/channel/magazine_ecomm')
    	self.assertEqual(response.status, "200 OK" )

    def test_channel_invalid_param(self):
    	response =  self.app.get('/channel/magazine_ecomm?end=2016-03-18')
    	self.assertEqual(response.status, "400 BAD REQUEST" )

    def test_department_none(self):
        response =  self.app.get('/department/x')
        self.assertEqual(response.status, "200 OK" )

    def test_department_full_param(self):
        response =  self.app.get('/department/AR?begin=2016-03-17&end=2016-03-18')
        
        self.assertEqual(response.status, "200 OK")

    def test_department_half_param(self):
        response =  self.app.get('/department/AR?begin=2016-03-17')
        self.assertEqual(response.status, "200 OK" )
 
    def test_department_none_param(self):
        response =  self.app.get('/department/AR')
        self.assertEqual(response.status, "200 OK" )

    def test_department_invalid_param(self):
        response =  self.app.get('/department/AR?end=2016-03-18')
        self.assertEqual(response.status, "400 BAD REQUEST" )


if __name__ == "__main__":
    unittest.main()