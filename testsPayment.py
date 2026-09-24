#!/usr/bin/env python3

import Payment
import Order
from unittest.mock import patch
import unittest


class paymentTests(unittest.TestCase):
    @patch('builtins.print', wraps=print)
    def test_pix_payment(self, mock_print):
        # Test the pix payment messages
        print("\nTeste com pix:")
        order = (
            Order.OrderBuilder(Order.Order)
            .set_client(Order.Client("Ada Lovelace"))
            .set_pay_method(Payment.PixPayment())
            .build()
        )
        order.pay_method.pay(10.0)
        
        mock_print.assert_called_with("Pagou-se R$10.0 com PIX")


    @patch('builtins.print', wraps=print)
    def test_creditCard_payment(self, mock_print):
        # Test the pix credit card messages
        print("\nTeste com cartão de crédito:")
        order = (
            Order.OrderBuilder(Order.Order)
            .set_client(Order.Client("Ada Lovelace"))
            .set_pay_method(Payment.CreditCardPayment())
            .build()
        )
        order.pay_method.pay(10.0)
        mock_print.assert_called_with("Pagou-se R$10.0 com cartão de crédito")


if __name__ == "__main__":
    unittest.main()