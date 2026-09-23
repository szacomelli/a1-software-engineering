#!/usr/bin/env python3

import Payment
#import Order

class MockOrder:
    payment_method = None

    def __init__(self, pm):
        self.payment_method = pm

    def total(self):
        return 10

order = MockOrder("PIX")

pix = Payment.PixProcessor().process_order(order)
credit_card = Payment.CreditCardProcessor().process_order(order)

# teste 2 não faz sentido???
processor = None
if order.payment_method == "PIX":
    processor = Payment.PixProcessor()
elif order.payment_method == "cartão de crédito":
    processor = Payment.CreditCardProcessor()
else:
    processor = Payment.BoletoProcessor()

processor.process_order(order)
