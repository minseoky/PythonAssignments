class Cocktail:
    def __init__(self, name):
        self.ingredients = []
        self.name = name

    def input_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def show_ingredients(self):
        index = 1
        print("+::%s's Ingredients::+" % self.name)
        for i in self.ingredients:
            print("%d : %s" % (index, i))
            index += 1


class TequilaBased(Cocktail):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        TequilaBased.count += 1

    def show_ingredients(self):
        index = 1
        print("+::%s's Ingredients(Tequila Based)::+" % self.name)
        for i in self.ingredients:
            print("%d : %s" % (index, i))
            index += 1

    @staticmethod
    def show_count():
        print("We have %d Tequila Type" % TequilaBased.count)


class RumBased(Cocktail):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        RumBased.count += 1

    def show_ingredients(self):
        index = 1
        print("+::%s's Ingredients(Rum Based)::+" % self.name)
        for i in self.ingredients:
            print("%d : %s" % (index, i))
            index += 1

    @staticmethod
    def show_count():
        print("We have %d Rum Type" % RumBased.count)



#----------------------TequilaBased----------------------

tequila_sunrise = TequilaBased("Tequila Sunrise")
tequila_sunrise.ingredients = ["1 1/2 ounces tequila", "3/4 cup orange juice",
                               "3/4 ounce grenadine syrup", "Orange slice, for garnish",
                               "High-quality maraschino cherry, such as Luxardo, for garnish"]

#--------------------------------------------------------

#------------------------RumBased------------------------

long_island_iced_tea = RumBased("Long Island Iced Tea")
long_island_iced_tea.ingredients = ["½ fluid ounce vodka", "½ fluid ounce rum",
                                    "½ fluid ounce gin", "½ fluid ounce tequila",
                                    "½ fluid ounce triple sec (orange-flavored liqueur)",
                                    "1 fluid ounce sweet and sour mix",
                                    "1 fluid ounce cola, or to taste", "1 lemon slice"]

#--------------------------------------------------------