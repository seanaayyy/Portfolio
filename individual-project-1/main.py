from Ingredient import Ingredient
from Cocktail import Cocktail
from RecipeBook import RecipeBook

def main():
    cocktail_list = []
    available_ingredients = []
    available_cocktails = []

    # add all the ingredients I have available :)
    available_ingredients.append(Ingredient('Vodka', True, ''))
    available_ingredients.append(Ingredient('Gin', True, ''))
    available_ingredients.append(Ingredient('Sugar', True, ''))
    available_ingredients.append(Ingredient('Lime', True, ''))
    available_ingredients.append(Ingredient('Yellow Chartreuse', True, ''))
    available_ingredients.append(Ingredient('Campari', True, ''))
    available_ingredients.append(Ingredient('Sweet Vermouth', True, ''))
    available_ingredients.append(Ingredient('Angostura bitters', True, ''))
    available_ingredients.append(Ingredient('Triple sec', True, ''))
    available_ingredients.append(Ingredient('Cranberry juice', True, ''))
    available_ingredients.append(Ingredient('Lime juice', True, ''))
    available_ingredients.append(Ingredient('Lemon juice', True, ''))
    available_ingredients.append(Ingredient('Scotch', True, ''))
    available_ingredients.append(Ingredient('Drambuie', True, ''))
    available_ingredients.append(Ingredient('Orange bitters', True, ''))
    available_ingredients.append(Ingredient('Grand Marnier', True, ''))
    available_ingredients.append(Ingredient('Brandy', True, ''))
    available_ingredients.append(Ingredient('Cognac', True, ''))
    available_ingredients.append(Ingredient('St. Germain', True, ''))
    available_ingredients.append(Ingredient('Rye whiskey', True, ''))
    available_ingredients.append(Ingredient('Malibu rum', True, ''))
    available_ingredients.append(Ingredient('Spiced rum', True, ''))
    available_ingredients.append(Ingredient('Lime peel', True, ''))
    available_ingredients.append(Ingredient('Orange', True, ''))
    available_ingredients.append(Ingredient('Orange peel', True, ''))
    available_ingredients.append(Ingredient('Lemon peel', True, ''))
    available_ingredients.append(Ingredient('Lemon juice', True, ''))

    # create RecipeBook object, load data from csv file, and print out available cocktails
    book = RecipeBook(cocktail_list, available_ingredients, available_cocktails)
    book.load_data('all_drinks.csv')
    available_cocktails = book.get_available_cocktails()
    for c in available_cocktails:
        print(c.to_string())

    # Find all cocktails with gin as its base
    base = Ingredient('Gin')
    gin_cocktails = book.find_cocktails_with_base(base)
    print('GIN DRINKS')
    for gc in gin_cocktails:
        print(gc.to_string())

if __name__ == "__main__":
    main()