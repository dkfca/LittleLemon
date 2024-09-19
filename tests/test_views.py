from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import now
from LittleLemonAPI.models import Menu, Booking

class ApiViewTest(TestCase):
    username = 'test1'
    password = '12345'
    email = 'test@littlelemon.com'

    def setUp(self) -> None:
        item = Menu.objects.create(
            title = 'IceCream1', 
            price = 81, 
            inventory = 101
        )
        item.save()
        item = Menu.objects.create(
            title = 'Pasta', 
            price = 82, 
            inventory = 102
        )
        item.save()

        booking = Booking.objects.create(
            name="Customer1",
            no_of_guest = 10,
            bookingDate = now()
        )
        booking.save()

        booking = Booking.objects.create(
            name="Customer2",
            no_of_guest = 100,
            bookingDate = now()
        )
        booking.save()

        test_user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        test_user.save()
    
    def get_token(self) -> dict:
        auth_response = self.client.post(path='/auth/token/login/', data={
            'username': self.username,
            'password': self.password
        }, follow=True)
        token = auth_response.json()['auth_token']
        auth_head = {
            'Authorization': f'Token {token}'
        }
        return auth_head
    
    def test_getall_menu_noauth(self) -> None:
        response = self.client.get(path='/api/menu/', follow=True)
        self.assertEqual(response.status_code, 401)

    def test_getall_menu(self) -> None:
        auth_head = self.get_token()
        response = self.client.get(path='/api/menu/', headers=auth_head, follow=True)
        response_json = response.json()
        for menu in response_json:
            self.assertIsNotNone(menu['title'])
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_json)

    def test_create_menu_noauth(self) -> None:
        data = {
            'title': 'Sausage',
            'price': 20,
            'inventory': 99
        }
        response = self.client.post(path='/api/menu/', 
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 401)
    
    def test_create_menu(self) -> None:
        auth_head = self.get_token()
        data = {
            'title': 'Sausage',
            'price': 20,
            'inventory': 99
        }
        response = self.client.post(path='/api/menu/', 
                                    headers=auth_head, 
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 201)
        menu = Menu.objects.get(title='Sausage')
        self.assertEqual(menu.title, 'Sausage')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.inventory, 99)
    
    def test_getall_bookings_noauth(self) -> None:
        response = self.client.get(path='/api/booking/', follow=True)
        self.assertEqual(response.status_code, 401)

    def test_getall_bookings(self) -> None:
        auth_head = self.get_token()
        response = self.client.get(path='/api/booking/', headers=auth_head, follow=True)
        response_json = response.json()
        for booking in response_json:
            self.assertIsNotNone(booking['name'])
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_json)
    
    def test_create_bookings_noauth(self) -> None:
        datum = now()
        data = {
            'name': "Customer3",
            'no_of_guest': 12,
            'bookingDate': datum
        }
        response = self.client.post(path='/api/booking/', 
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 401)
    
    def test_create_bookings(self) -> None:
        auth_head = self.get_token()
        datum = now()
        data = {
            'name': "Customer3",
            'no_of_guest': 12,
            'bookingDate': datum
        }
        response = self.client.post(path='/api/booking/', 
                                    headers=auth_head, 
                                    data=data,
                                    follow=True)
        self.assertEqual(response.status_code, 201)
        customer3 = Booking.objects.get(name='Customer3')
        self.assertEqual(customer3.no_of_guest, 12)
        self.assertEqual(customer3.name, 'Customer3')
        self.assertEqual(customer3.bookingDate, datum)