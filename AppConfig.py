#!/usr/bin/env python3


class AppConfig:
    environment = None
    currency = None
    debug = None
    __instance = None
    __created = False

    def __new__(cls, *args, **kargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, environment=None, currency=None, debug=False):
        if self.__created:
            return
        self.environment = environment
        self.currency = currency
        self.debug = debug
        self.__created = True
