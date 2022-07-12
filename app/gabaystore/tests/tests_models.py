import unittest
from django.test import TestCase
from gabaystore.models import Cloth

class ClothTest(unittest.TestCase):
    
    def test_cloth_setup(self):
        Cloth.objects.create(name='T-shirt Black One Piece', picture='T-Shirt.jpg', size='M', clothing_type='T-Shirt', price=10.00, amount=10)
        
    def test_return_name(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.name, 'T-shirt Black One Piece')    
    
    def test_return_picture(self):
        cloth = Cloth.objects.get(name='T-Shirt.jpg')
        self.assertEquals(cloth.picture, 'T-Shirt.jpg')
    
    def test_return_size(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.size, 'M')
        
    def test_return_clothing_type(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.clothing_type, 'T-Shirt')
        
    def test_return_price(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.price, 10.00)
    
    def test_return_amount(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.amount, 10)
    
    def test_return_slug(self):
        cloth = Cloth.objects.get(name='T-shirt Black One Piece')
        self.assertEquals(cloth.slug, 't-shirt-black-one-piece')
    

# class TestGabayStore(TestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)

#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         self.assertEquals(response.status_code, 200)

#     def test_contact_page_status_code(self):
#         response = self.client.get('/contact/')
#         self.assertEquals(response.status_code, 200)

#     def test_login_page_status_code(self):
#         response = self.client.get('/login/')
#         self.assertEquals(response.status_code, 200)

#     def test_register_page_status_code(self):
#         response = self.client.get('/register/')
#         self.assertEquals(response.status_code, 200)

#     def test_product_page_status_code(self):
#         response = self.client.get('/product/')
#         self.assertEquals(response.status_code, 200)

#     def test_cart_page_status_code(self):
#         response = self.client.get('/cart/')
#         self.assertEquals(response.status_code, 200)

#     def test_checkout_page_status_code(self):
#         response = self.client.get('/checkout/')
#         self.assertEquals(response.status_code, 200)

#     def test_order_page_status_code(self):
#         response = self.client.get('/order/')
#         self.assertEquals(response.status_code, 200)

#     def test_search_page_status_code(self):
#         response = self.client.get('/search/')
#         self.assertEquals(response.status_code, 200)

#     def test_profile_page_status_code(self):
#         response = self.client.get('/profile/')
#         self.assertEquals(response.status_code, 200)
