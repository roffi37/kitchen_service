from django.test import TestCase
from django.urls import reverse

from .forms import DishForm, DishTypeForm, CookForm, CookCreationForm
from .models import Cook, DishType, Dish
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.dish_type = DishType.objects.create(name='Test Dish Type')
        self.dish = Dish.objects.create(name='Test Dish', description='Test Description', price=10.5, dish_type=self.dish_type)
        self.cook = Cook.objects.create(username='cooktest', years_of_experience=5)
        self.dish.cooks.add(self.cook)

    def test_dish_creation(self):
        dish = Dish.objects.get(name='Test Dish')
        self.assertEqual(dish.description, 'Test Description')
        self.assertEqual(dish.price, 10.5)
        self.assertEqual(dish.dish_type.name, 'Test Dish Type')
        self.assertEqual(dish.cooks.first().username, 'cooktest')

    def test_cook_creation(self):
        cook = Cook.objects.get(username='cooktest')
        self.assertEqual(cook.years_of_experience, 5)

    def test_dish_type_creation(self):
        dish_type = DishType.objects.get(name='Test Dish Type')
        self.assertEqual(dish_type.name, 'Test Dish Type')

    def test_str_methods(self):
        self.assertEqual(str(self.user), 'testuser')
        self.assertEqual(str(self.dish_type), 'Test Dish Type')
        self.assertEqual(str(self.dish), 'Test Dish')
        self.assertEqual(str(self.cook), 'cooktest')


class TestViews(TestCase):
    def setUp(self):
        self.user = Cook.objects.create(username='testuser')
        self.dish_type = DishType.objects.create(name='Test Dish Type')
        self.dish = Dish.objects.create(name='Test Dish', description='Test Description', price=10.5,
                                        dish_type=self.dish_type)

    def test_dish_list_view(self):
        response = self.client.get(reverse('kitchen:dishes-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['dish_list'], Dish.objects.all(), ordered=False)

    def test_dish_create_view(self):
        data = {
            'name': 'New Dish',
            'description': 'New Description',
            'price': 15.0,
            'dish_type': self.dish_type.id
        }
        response = self.client.post(reverse('kitchen:dish-create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name='New Dish').exists())


class TestForms(TestCase):
    def test_dish_type_form(self):
        form = DishTypeForm(data={
            'name': 'Test Dish Type',
        })

        self.assertTrue(form.is_valid())

    def test_cook_form(self):
        form = CookForm(data={
            'years_of_experience': 3,
            'first_name': 'John',
            'last_name': 'Doe'
        })

        self.assertTrue(form.is_valid())

    def test_cook_creation_form(self):
        form = CookCreationForm(data={
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
            'years_of_experience': 5,
        })

        self.assertTrue(form.is_valid())
