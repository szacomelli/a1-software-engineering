#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self):
        pass

    # def process_order(self, order):
    #     payment = self.create_payment()
    #     payment.pay(order.total())
    def process_order(self, order):
        order.pay_method = self.create_payment()
        payment.pay(order.total())


class PixPayment(Payment):
    def pay(self, amount):
        print(f"Pagou-se R${amount} com PIX")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Pagou-se R${amount} com cartão de crédito")

class BoletoPayment(Payment):
    def pay(self, amount):
        print(f"Pagou-se R${amount} com boleto")


class PixProcessor(PaymentProcessor):
    def create_payment(self):
        return PixPayment()

class CreditCardProcessor(PaymentProcessor):
    def create_payment(self):
        return CreditCardPayment()

class BoletoProcessor(PaymentProcessor):
    def create_payment(self):
        return BoletoPayment()
