import unittest
import Order


class orderTests(unittest.TestCase):
  def test_without_client(self):
    # Test if the build without a client raises an error
    builder = Order.OrderBuilder(Order.Order)
    with self.assertRaises(ValueError):
      builder.build()


  def test_with_two_attributes(self):
    # Testing build with two optional attributes
    builder = Order.OrderBuilder(Order.Order)
    order = (
      builder.set_client(Order.Client("Ada Lovelace"))
      .set_address("Avenida da Fúria")
      .set_coupon("TOPCUPOM")
      .build()
      )
    
    self.assertEqual(order.address, "Avenida da Fúria")
    self.assertEqual(order.coupon, "TOPCUPOM")
    self.assertEqual(order.observation, None)
    self.assertEqual(order.pay_method, None)


  def test_with_two_items(self):
    # Testing build with two items
    builder = Order.OrderBuilder(Order.Order)
    order = (
      builder.set_client(Order.Client("Ada Lovelace"))
      .add_product(Order.Product("Kinder Bueno", 11.69, 27))
      .add_product(Order.Product("Casa básica", 1_000_000_000.00, 1))
      .build()
    )

    self.assertGreater(order.total(), 0.0)
    self.assertEqual(len(order.products), 2)


if __name__ == '__main__':
    unittest.main()