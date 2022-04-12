# cocktail: the recipe book has instances of cocktail
from Ingredient import Ingredient

class Cocktail:
    def __init__(self, name, alcoholic = True, glass = '', ingredients = []):
        self.name = name
        self.alcoholic = alcoholic
        self.glass = glass
        self.ingredients = ingredients

    def to_string(self):
        s = "Name:\n" + self.name + "\n\nIngredients:\n"
        for obj in self.ingredients:
            s += obj.get_measurement() + "  " + obj.get_name() + "\n"
        s += '----------------------------------------------'
        return s

    def get_name(self):
        return self.name

    def get_alcoholic(self):
        return self.alcoholic

    def get_glass(self):
        return self.glass

    def get_ingredients(self):
        return self.ingredients
