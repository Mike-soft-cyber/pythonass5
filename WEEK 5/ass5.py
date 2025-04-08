#Activity One
class Food:
    def __init__(self, lunch, desert, refreshments):
        self.lunch = lunch
        self.desert = desert
        self.refreshements = refreshments

class Favourite(Food):
    pass

food = Food("pizza", "Milkshake", "Soda")
print(food.lunch)
print(food.desert)
print(food.refreshements)

#Activity two

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Animal:
    def move(self):
        return "Walking"

for action in [Car(), Plane(), Animal()]:
    print(action.move())