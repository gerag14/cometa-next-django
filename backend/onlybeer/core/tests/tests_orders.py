from django.test import TestCase

from .models import Order, OrderItem, Product


class OrderItemTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name="Producto 1", price=10, stock=5)
        self.product2 = Product.objects.create(name="Producto 2", price=20, stock=3)
        self.product3 = Product.objects.create(name="Producto 3", price=30, stock=0)

        self.order = Order.objects.create(customer="Cliente de prueba")

    def test_order_item_creation(self):  # noqa
        order_item1 = OrderItem.objects.create(
            order=self.order, product=self.product1, quantity=2
        )
        self.assertEqual(order_item1.total, 20)

        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                order=self.order, product=self.product2, quantity=5
            )

        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                order=self.order, product=self.product3, quantity=1
            )

        initial_stock = self.product1.stock
        OrderItem.objects.create(order=self.order, product=self.product1, quantity=1)
        self.assertEqual(self.product1.stock, initial_stock - 1)

        initial_stock = self.product2.stock
        with self.assertRaises(ValueError):
            OrderItem.objects.create(
                order=self.order, product=self.product2, quantity=5
            )
        self.assertEqual(self.product2.stock, initial_stock)

    def test_order_total_calculation(self):  # noqa
        OrderItem.objects.create(order=self.order, product=self.product1, quantity=2)

        OrderItem.objects.create(order=self.order, product=self.product2, quantity=1)

        self.assertEqual(self.order.total, 40)

        OrderItem.objects.create(order=self.order, product=self.product3, quantity=1)

        self.assertEqual(self.order.total, 40)

        self.product3.stock = 1
        self.product3.save()
        self.assertEqual(self.order.total, 70)
