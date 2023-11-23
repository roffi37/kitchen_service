from unittest import TestCase

from kitchen.forms import DishTypeForm


class DishTypeFormTest(TestCase):
    def test_dish_type_form_valid_data(self):
        form = DishTypeForm(data={'name': 'Test Course'})
        self.assertTrue(form.is_valid())

    def test_dish_type_form_no_data(self):
        form = DishTypeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
