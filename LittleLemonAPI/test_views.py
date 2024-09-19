from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        item1 = MenuItem.objects.create(
            title = 'IceCream1', 
            price = 81, 
            inventory = 101
        )
        item1.save()
        item2 = MenuItem.objects.create(
            title = 'IceCream2', 
            price = 82, 
            inventory = 102
        )
        item2.save()

        test_user = User.objects.create_user(
            username='test1',
            email='test@tes.com',
            password='12345',
        )
        test_user.save()

    def test_getall(self) -> None:
        auth_response = self.client.post(path='/auth/token/login/', data={
            'username': 'test1',
            'password': '12345'
        }, follow=True)
        token = auth_response.json()['auth_token']
        head = {
            'Authorization': "Token " + token
        }
        response = self.client.get(path='/api/menu-items/', 
                                   headers=head, 
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())