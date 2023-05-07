from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        # Створити користувача з валідними логіном та паролем
        self.user = User.objects.create_user('Olha', password='Jkmuf2002')

    def test_login(self):
        # Відкрити сторінку авторизації
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

        # Ввести валідний логін та пароль
        response = self.client.post('/login/', {'username': 'Olha', 'password': 'Jkmuf2002'})

        # Перевірити, що користувач успішно авторизований
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
