from Cocktail import Cocktail
from Ingredient import Ingredient
import csv

class RecipeBook:
    s_recipe_book = None

    @classmethod
    def get(self):
        if self.s_recipe_book is None:
            self.s_recipe_book = RecipeBook()
        return self.s_recipe_book

    def __init__(self, cocktails = [], available_ingredients: [] = [], available_cocktails: [] = []):
        self.cocktails = cocktails
        self.available_ingredients = available_ingredients
        self.available_cocktails = available_cocktails

    def get_cocktails(self):
        return self.cocktails

    def get_available_ingredients(self):
        self.find_cocktails()
        return self.available_ingredients

    def get_available_cocktails(self):
        self.find_cocktails()
        return self.available_cocktails

    def set_available_ingredients(self, ingredients):
        self.available_ingredients = ingredients

    def clear_ingredients(self):
        self.available_ingredients.clear()
        self.available_cocktails.clear()

    # sets available_cocktails depending on available_ingredients
    def find_cocktails(self):
        self.available_cocktails.clear()
        # check every cocktail in the book
        for c in self.cocktails:
            add_cocktail = True
            for i in c.get_ingredients():
                ingredient_found = False
                for ai in self.available_ingredients:
                    # ingredient is found if it is available or if it is blank
                    if i.get_name().strip() == ai.get_name() or not bool(i.get_name()):
                        ingredient_found = True
                if not ingredient_found:
                    add_cocktail = False
            if add_cocktail:
                self.available_cocktails.append(c)

    # incorrect implementation of find_cocktails
    def find_cocktails_incorrect(self):
        self.available_cocktails.clear()
        # check every cocktail in the book
        for c in self.cocktails:
            add_cocktail = True
            ingredient_found = False # INCORRECT IMPLEMENTATION
            for i in c.get_ingredients():
                for ai in self.available_ingredients:
                    # ingredient is found if it is available or if it is blank
                    if i.get_name().strip() == ai.get_name() or not bool(i.get_name()):
                        ingredient_found = True
                if not ingredient_found:
                    add_cocktail = False
            if add_cocktail:
                self.available_cocktails.append(c)

    def find_cocktails_with_base(self, ing: Ingredient):
        list = []
        for c in self.cocktails:
            if c.get_ingredients()[0].get_name() == ing.get_name():
                list.append(c)
        return list

    def cocktail_available(self, cocktail: Cocktail):
        available = False
        for c in self.cocktails:
            if cocktail.get_name() == c.get_name():
                available = True
        return available

    # read csv file into Cocktail objects
    def load_data(self, file):
        with open(file, newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None) # skips the header
            for name, alcoholic, glass, ingr1, ingr2, ingr3, ingr4, ingr5, ingr6, ingr7, ingr8, ingr9, ingr10, ingr11, ingr12, meas1, meas2, meas3, meas4, meas5, meas6, meas7, meas8, meas9, meas10, meas11, meas12 in reader:
                # create ingredient objects
                ingredients = []
                available = False
                ingredient1 = Ingredient(ingr1, available, meas1)
                ingredients.append(ingredient1)
                ingredient2 = Ingredient(ingr2, available, meas2)
                ingredients.append(ingredient2)
                ingredient3 = Ingredient(ingr3, available, meas3)
                ingredients.append(ingredient3)
                ingredient4 = Ingredient(ingr4, available, meas4)
                ingredients.append(ingredient4)
                ingredient5 = Ingredient(ingr5, available, meas5)
                ingredients.append(ingredient5)
                ingredient6 = Ingredient(ingr6, available, meas6)
                ingredients.append(ingredient6)
                ingredient7 = Ingredient(ingr7, available, meas7)
                ingredients.append(ingredient7)
                ingredient8 = Ingredient(ingr8, available, meas8)
                ingredients.append(ingredient8)
                ingredient9 = Ingredient(ingr9, available, meas9)
                ingredients.append(ingredient9)
                ingredient10 = Ingredient(ingr10, available, meas10)
                ingredients.append(ingredient10)
                ingredient11 = Ingredient(ingr11, available, meas11)
                ingredients.append(ingredient11)
                ingredient12 = Ingredient(ingr12, available, meas12)
                ingredients.append(ingredient12)

                # add cocktail to list
                self.cocktails.append(Cocktail(name, alcoholic, glass, ingredients))
