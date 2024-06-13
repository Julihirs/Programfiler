class Person():
    def __init__(self):
        self.name = ""
        self.money = 0
 
bob = Person()
bob.name = "Bob"
bob.money = 100
 
nancy = Person()
nancy.name = "Nancy"
 
print(bob.name, "has", bob.money, "dollars.")
print(nancy.name, "has", nancy.money, "dollars.")


def give_money2(person):
    person.money += 100
 
give_money2(bob)
print(bob.money)



class Cat():
    name = ""
    color = ""
    weight = 0

    def meow(self):
        print(self.name, "says 'meow'")

cat = Cat()
cat.name = "Eros"
cat.color = "black"
cat.weight = 4

cat.meow()

print(cat.name, "weighs", cat.weight, "kg")
print(cat.name, "is", cat.color)