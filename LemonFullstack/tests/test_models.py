import unittest
from django.test import TestCase
from restaurant.models import MenuItem
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = MenuItem.objects.create(
            title = 'Pizza',
            price = 8.99,
            inventory = 15
        )

    def test_create_menu_item(self) -> None:
        item2 = MenuItem.objects.create(
            title = 'Burger',
            price = 5.99,
            inventory = 10
        )
        self.assertEqual(MenuItem.objects.count(), 2)
        self.assertEqual(item2.title, 'Burger')
        self.assertEqual(item2.price, Decimal(5.99))
        self.assertEqual(item2.inventory, 10)

    def test_get_menu_item(self) -> None:
        item = MenuItem.objects.get(id = self.item1.id)
        self.assertEqual(item.title, 'Pizza')
        self.assertEqual(item.price, Decimal(8.99).quantize(Decimal("0.00")))
        self.assertEqual(item.inventory, 15)

    def test_delete_menu_item(self) -> None:
        item = MenuItem.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(MenuItem.objects.count(), 0)
