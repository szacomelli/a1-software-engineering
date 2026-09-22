#!/usr/bin/env python3

import AppConfig as ac

obj1 = ac.AppConfig()
obj2 = ac.AppConfig("asdasd", "USD", True)

# testing if they point to the same object
print(obj1 == obj2)

# testing if __init__ of obj2 didnt overwrite
# the obj1 attributes
print(obj2.environment)
print(obj2.currency)
print(obj2.debug)

# testing if obj2 "follow" changes made by obj1
obj1.currency = "Mangos"
print(obj2.currency)
