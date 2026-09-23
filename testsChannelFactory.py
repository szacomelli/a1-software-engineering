#!/usr/bin/env python3

import ChannelFactory

class MockOrder:
    def __str__(self):
        return f"ordem e progresso"

fact = ChannelFactory.WebFactory()
checkout = fact.create_checkout()
notification = fact.create_notification()

checkout.show(MockOrder())
notification.send(MockOrder())

fact = ChannelFactory.get_channel_factory("MOBILE")
checkout = fact.create_checkout()
notification = fact.create_notification()

checkout.show(MockOrder())
notification.send(MockOrder())

fact = ChannelFactory.get_channel_factory("KIOSK")
checkout = fact.create_checkout()
notification = fact.create_notification()

checkout.show(MockOrder())
notification.send(MockOrder())

ChannelFactory.get_channel_factory("")
