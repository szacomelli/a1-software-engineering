#!/usr/bin/env python3

import AppConfig as ac
import unittest


class appConfigTests(unittest.TestCase):
  def test_uniqueness(self):
    # Testing appConfig uniqueness 
    obj1 = ac.AppConfig()
    obj2 = ac.AppConfig()
    self.assertEqual(obj1, obj2)


  def test_changes_follow(self):
    # Testing if a change in a reference are kept in another
    obj1 = ac.AppConfig()
    obj2 = ac.AppConfig()
    obj1.currency = "EUR"
    self.assertEqual(obj2.currency, "EUR")


  def test_no_overwrite(self):
    # Testing if init didn't overwrite
    obj1 = ac.AppConfig()
    obj1.currency = "USD"
    obj2 = ac.AppConfig(currency="SDKFNSK")
    self.assertEqual(obj2.currency, "USD")
    

if __name__ == "__main__":
  ac.AppConfig("production", "BRL", False)
  unittest.main()