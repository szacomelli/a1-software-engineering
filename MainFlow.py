#!/usr/bin/env python3
import AppConfig, Order, Payment, ChannelFactory

class BuildSampleOrder:
    def build_grocery_order():
        maca = Order.Product("Maçã", 1.00, 4)
        macarrao = Order.Product("Macarrão", 3.99, 6)
        return (Order.OrderBuilder(Order.Order)
             .set_client(Order.Client("Ada Lovelace"))
             .set_address("Rua Voluntários da Pátria")
             .set_coupon("OMELHORCUPOM")
             #.set_pay_method(self.processor.create_payment())
             .set_observation("Pedido deve ser entregue com urgência")
             .add_product(maca)
             .add_product(macarrao)
             .add_product_by_name("Pera", 0.80, 3)
             .build())

class Flow:
    processor = None
    def __init__(self, available_channels, processor):
        self.processor = processor
        ChannelFactory.available_channels = available_channels

    def main(self, channel, get_order):
        config = AppConfig.AppConfig("production", "BRL", True)

        order = get_order()

        channel_factory = ChannelFactory.get_channel_factory(channel)
        checkout = channel_factory.create_checkout()
        notification = channel_factory.create_notification()

        checkout.show(order)
        self.processor.process_order(order)
        notification.send(order)

        if config.debug:
            self.save_log()

        return

    def save_log(self):
        print("log foi salvo")


channels = {
            "WEB" : ChannelFactory.WebFactory,
            "MOBILE" : ChannelFactory.MobileFactory,
            "KIOSK" : ChannelFactory.KioskFactory
        }
chosen_processor = Payment.PixProcessor()

Flow(channels, chosen_processor).main("WEB", BuildSampleOrder.build_grocery_order)
