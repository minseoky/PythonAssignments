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
        self.ingredients = []
        self.name = name
        TequilaBased.count += 1

    def show_ingredients(self):
        index = 1
        print("+::%s's Ingredients(Tequila Based)::+" % self.name)
        for i in self.ingredients:
            print("%d : %s" % (index, i))
            index += 1

    def show_count(self):
        print("We have %d Tequila Type" % TequilaBased.count)


# tequila_sunrise.show_ingredients()

tequila_sunrise = TequilaBased("Tequila Sunrise")
tequila_sunrise.ingredients = ["1 1/2 ounces tequila", "3/4 cup orange juice",
                               "3/4 ounce grenadine syrup", "Orange slice, for garnish",
                               "High-quality maraschino cherry, such as Luxardo, for garnish"]
