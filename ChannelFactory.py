#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Checkout(ABC):
    @abstractmethod
    def show(self, order):
        pass

class Notification(ABC):
    @abstractmethod
    def send(self, order):
        pass

class ChannelFactory(ABC):
    @abstractmethod
    def create_checkout(self):
        pass

    @abstractmethod
    def create_notification(self):
        pass


class WebCheckout(Checkout):
    def show(self, order):
        print("Pedido feito pela web, para a web:")
        print(order)

class WebNotification(Notification):
    def send(self, order):
        print("Notificação de pedido mandado para o browser!")
        print(order)

class WebFactory(ChannelFactory):
    def create_checkout(self):
        return WebCheckout()

    def create_notification(self):
        return WebNotification()


class MobileCheckout(Checkout):
    def show(self, order):
        print("Pedido feito no Mobile:")
        print(order)

class MobileNotification(Notification):
    def send(self, order):
        print("Notificação de pedido mandado para a palma da mão!")
        print(order)

class MobileFactory(ChannelFactory):
    def create_checkout(self):
        return MobileCheckout()

    def create_notification(self):
        return MobileNotification()
