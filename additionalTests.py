import unittest
import AppConfig
import Order
import ChannelFactory


AppConfig.AppConfig("production", "BRL", False)


class testSingleton(unittest.TestCase):
  # Aditional tests for the singleton

  def test_types(self):
    # Verifies if the var types are correct
    config = AppConfig.AppConfig()
    self.assertIsInstance(AppConfig.AppConfig, type)
    self.assertIsInstance(config, AppConfig.AppConfig)
    self.assertIsInstance(config.currency, str)
    self.assertIsInstance(config.environment, str)
    self.assertIsInstance(config.debug, bool)


  def test_currency(self):
    # Aditional test: Verifies if the currency is one of the allowed
    known_currency = ["USD", "BRL", "EUR", "JPY"]
    config = AppConfig.AppConfig()
    self.assertIn(config.currency, known_currency)


class testBuilder(unittest.TestCase):
  # Aditional tests for the builder

  def test_types(self):
    # Verifies if the var/order types are correct
    builder = Order.OrderBuilder(Order.Order)
    order = (
      builder.set_client(Order.Client("Ada Lovelace"))
      .set_address("Parquinho da Pekka")
      .set_coupon("1010SHOPEE")
      .add_product(Order.Product("Gemas Clash Royale", 53.90, 2500))
      .build()
    )
    self.assertIsInstance(order, Order.Order)
    self.assertIsInstance(order.client, Order.Client)
    self.assertIsInstance(order.products[0], Order.Product)


  def test_values(self):
    # Aditional test: Verifies if the inputs are set
    builder = Order.OrderBuilder(Order.Order)
    order = (
      builder.set_client(Order.Client("Ada Lovelace"))
      .set_address("Parquinho da Pekka")
      .set_coupon("1010SHOPEE")
      .add_product(Order.Product("Gemas Clash Royale", 53.90, 2500))
      .build()
    )

    self.assertEqual(order.client.name, "Ada Lovelace")
    self.assertEqual(order.address, "Parquinho da Pekka")
    self.assertEqual(order.coupon, "1010SHOPEE")
    self.assertEqual(f"{order}", f"Client name: Ada Lovelace\nCoupon used: 1010SHOPEE\nAddress inputed: Parquinho da Pekka\nProducts:\n - 1: Gemas Clash Royale; Quantity: 2500; Price: 53.90\n")


class testFabric(unittest.TestCase):
  # Aditional tests for the fabric

  def test_types(self):
    # Tests the checkout and notification are created correctly
    factory = ChannelFactory.WebFactory()
    checkout = factory.create_checkout()
    notification = factory.create_notification()
    self.assertIsInstance(checkout, ChannelFactory.WebCheckout)
    self.assertIsInstance(notification, ChannelFactory.WebNotification)


if __name__ == '__main__':
    unittest.main()