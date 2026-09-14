class Food:
    def calculate_price(self):
        pass


class Pizza(Food):
    def calculate_price(self):
        return 250


class Burger(Food):
    def calculate_price(self):
        return 150


class Biryani(Food):
    def calculate_price(self):
        return 200


class Sandwich(Food):
    def calculate_price(self):
        return 100


foods = [Pizza(), Burger(), Biryani(), Sandwich()]

for food in foods:
    print("Price:", food.calculate_price())