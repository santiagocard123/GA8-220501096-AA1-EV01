from flask_pymongo import PyMongo

mongo = PyMongo()

class Component:
    def __init__(self, name, type_, brand, price):
        self.name = name
        self.type = type_
        self.brand = brand
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "brand": self.brand,
            "price": self.price,
        }