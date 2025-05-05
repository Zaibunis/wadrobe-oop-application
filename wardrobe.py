import json

class ClothingItem:
    def __init__(self, name, color, type, size, price, images):
        self.name = name
        self.color = color
        self.type = type
        self.size = size
        self.price = price
        self.images = images   

class Wardrobe:
    def __init__(self, items):
        self.items = [ClothingItem(**item) for item in items]


    def get_by_color(self, color):
        return [item for item in self.items if item.color == color]

class Mood:
    mood_color_map = {
        "Happy": "yellow",
        "Sad": "blue",
        "Angry": "red",
        "Relaxed": "green"
    }

    @classmethod
    def get_color(cls, mood):
        return cls.mood_color_map.get(mood, "black")

class User:
    def __init__(self, name):
        self.name = name
