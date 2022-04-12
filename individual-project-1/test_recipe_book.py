import unittest
from Cocktail import Cocktail
from Ingredient import Ingredient
from RecipeBook import RecipeBook

# Define a class that is subclassed from unittest.Testcase
#
# There are four functions you can implement
#
# (1) static member function setUpClass()
# - this will be called one time, before any tests run
# - the cls parameter will be an instance of this class:
#   it's how you can refer to member variables
# - this is a useful one--you can set things up here for your tests
#
# (2) static member function tearDownClass()
# - do any cleanup you need (you might not need to do any; so in this case
#   you don't have to implement the function
#
# (3) setUp()
# - called before each test
# - if you don't need to do anything before each test, then don't implement this
#
# (4) tearDown()
# - called after each test
# - I use this to clean up after each test
# - but again, if you don't need to do any cleanup after each tests,
#   then don't implement this
#
# in PyCharm, you can run your tests by right-clicking on your test file
# and then doing "Run Unittests in [your filename]
#
# View -> Tool Windows -> Run will show you the results of your tests
#
# If you are running this from the command line, then include these
# lines in your test code (without the comment chars):
#
# if __name__ == "__main__":
#  unittest.main()

class TestFindCocktails(unittest.TestCase):
    RecipeBook = None

    @classmethod
    def setUpClass(cls):
        # called one time, at the very beginning
        print('setUpClass()')
        cls.RecipeBook = RecipeBook().get()

        # create a few ingredients
        ingr1 = Ingredient('Gin')
        ingr2 = Ingredient('Tonic water')
        ingr3 = Ingredient('Lime')
        ingr4 = Ingredient('Triple sec')

        # load cocktails into recipe book
        cls.RecipeBook.load_data('all_drinks.csv')


        # we'll use the available ingredients to test, so add them to recipe book
        cls.RecipeBook.set_available_ingredients([ingr1, ingr2, ingr3, ingr4])

    @classmethod
    def tearDownClass(cls):
        # called one time, at the very end--if you need to do any final cleanup, do it here
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')
        self.RecipeBook.clear_ingredients()
        ingr1 = Ingredient('Gin')
        ingr2 = Ingredient('Tonic water')
        ingr3 = Ingredient('Lime')
        ingr4 = Ingredient('Triple sec')
        self.RecipeBook.set_available_ingredients([ingr1, ingr2, ingr3, ingr4])

    def tearDown(self):
        # called after every test
        print('tearDown()')
        self.RecipeBook.clear_ingredients()

    # -------------------------------------------------------------

    def test_find_cocktails_incorrect(self):
        print('test find cocktails incorrect')
        # this tests the incorrect version of find_cocktails

        # check that available cocktails is empty
        cocktails = self.RecipeBook.get_available_cocktails()
        self.assertEqual(len(self.RecipeBook.get_available_cocktails()), 0)

        # call incorrect implementation of find_cocktails
        self.RecipeBook.find_cocktails_incorrect()

        # check that first cocktail is the 'Flying Dutchman' - this will fail
        self.assertEqual(self.RecipeBook.get_available_cocktails()[0].get_name(), 'Flying Dutchman')

        # check that the second cocktail is a 'Gin And Tonic' - will also fail
        self.assertEqual(self.RecipeBook.get_available_cocktails()[1].get_name(), 'Gin And Tonic')

    #-------------------------------------------------------------

    def test_set_available_ingredients(self):
        print('test set available ingredients')
        # this tests the correct implemenation of find cocktails from recipe book: it will succeeed

        # RecipeBook has already been loaded with all cocktail recipes and available ingredients.
        # Call get_available_ingredients to make sure the ingredients are all there
        ingredients = self.RecipeBook.get_available_ingredients()
        self.assertEqual(len(ingredients), 4)

        # clear the available ingredients, make sure available_ingredients.lne() == 0
        self.RecipeBook.clear_ingredients()
        self.RecipeBook.find_cocktails()
        self.assertEqual(len(self.RecipeBook.get_available_ingredients()), 0)

    #-------------------------------------------------------------

    def test_find_cocktails(self):
        print('test find cocktails')
        # check that available cocktails is empty
        cocktails = self.RecipeBook.get_available_cocktails()
        self.assertEqual(len(self.RecipeBook.get_available_cocktails()), 0)

        # call find_cocktails, which will populate available_cocktails based on the 4 ingredients available (set in setUp)
        self.RecipeBook.find_cocktails()

        # check that the available cocktails are 'Flying Dutchman' and 'Gin And Tonic'
        available_cocktails = self.RecipeBook.get_available_cocktails()
        self.assertEqual(available_cocktails[0].get_name(), 'Flying Dutchman')
        self.assertEqual(available_cocktails[1].get_name(), 'Gin And Tonic')

        # clear available_ingredients and check that available_cocktails is also empty
        self.RecipeBook.clear_ingredients()
        available_cocktails = self.RecipeBook.get_available_cocktails()
        self.assertEqual(len(available_cocktails), 0)

    #-------------------------------------------------------------

    def test_find_cocktails_with_base(self):
        print('test find cocktails with gin base')
        # create ingredient 'Gin' that will be passed into this method
        gin = Ingredient('Gin')

        # call find_cocktails_with_base(gin) and check that each cocktail's first ingredient is gin
        gin_cocktails = self.RecipeBook.find_cocktails_with_base(gin)

        # check that list is not empty
        self.assertIsNotNone(gin_cocktails)

        # loop through list, verifying gin is in each cocktail
        for gc in gin_cocktails:
            self.assertEqual(gc.get_ingredients()[0].get_name(), 'Gin')

    def test_clear_ingredients(self):
        print('test clear ingredients')
        # recipe book already have four ingredients in it, check that is true
        self.assertEqual(len(self.RecipeBook.get_available_ingredients()), 4)

        # Now, clear the ingredients and check that available_ingredients is empty
        self.RecipeBook.clear_ingredients()
        self.assertEqual(len(self.RecipeBook.get_available_ingredients()), 0)

    def test_cocktail_available(self):
        print('test cocktail available')
        # call find_cocktails, which will populate available cocktails
        self.RecipeBook.find_cocktails()

        # 'Flying Dutchman' should be available
        self.assertTrue(self.RecipeBook.cocktail_available(Cocktail('Flying Dutchman')))

        # 'French 75' should not be available
        self.assertFalse(self.RecipeBook.cocktail_available(Cocktail('French 75')))

    # -------------------------------------------------------------

# if __name__ == "__main__":
# 	unittest.main2()