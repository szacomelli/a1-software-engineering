#!/usr/bin/env python3

import ChannelFactory
import Order
import Payment
from unittest.mock import patch, call
import unittest


class factoryTests(unittest.TestCase):
    @patch('builtins.print', wraps=print)
    def test_web_factory(self, mock_print):
        factory = ChannelFactory.WebFactory()
        checkout = factory.create_checkout()
        notification = factory.create_notification()

        order = (
            Order.OrderBuilder(Order.Order)
            .set_client(Order.Client("Ada Lovelace"))
            .set_pay_method(Payment.PixPayment)
            .build()
            )

        print("Teste do Web Checkout")
        checkout.show(order)

        print("Teste do Web Notification")
        notification.send(order)

        self.assertEqual(mock_print.call_count, 6)
        mock_print.assert_has_calls([
            call("Teste do Web Checkout"),
            call("Pedido feito pela web, para a web:"),
            call(order),
            call("Teste do Web Notification"),
            call("Notificação de pedido mandada para o browser!"),
            call(order),
        ])


    @patch('builtins.print', wraps=print)
    def test_mobile_factory(self, mock_print):
        factory = ChannelFactory.get_channel_factory("MOBILE")
        checkout = factory.create_checkout()
        notification = factory.create_notification()

        order = (
            Order.OrderBuilder(Order.Order)
            .set_client(Order.Client("Ada Lovelace"))
            .set_pay_method(Payment.CreditCardPayment)
            .build()
            )

        print("Teste do Mobile Checkout")
        checkout.show(order)

        print("Teste do Mobile Notification")
        notification.send(order)

        self.assertEqual(mock_print.call_count, 6)
        mock_print.assert_has_calls([
            call("Teste do Mobile Checkout"),
            call("Pedido feito no Mobile:"),
            call(order),
            call("Teste do Mobile Notification"),
            call("Notificação de pedido mandada para a palma da mão!"),
            call(order),
        ])


    def test_get_channel_error(self):
        with self.assertRaises(ValueError):
            ChannelFactory.get_channel_factory("")


if __name__ == "__main__":
  unittest.main()