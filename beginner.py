import random

# __init__ will loaded when the instance of this class is created.
# self refers to the object itself
# *args will pass various number of parameters and form them as a tuple
# To read tuple, one could use index to do that, i.e. args[0]
# **kwargs is similar with *arg, but it will form a dictionary.
# To read dic, one could use the key word to aceess it, i.e. kwargs["name"]

class FoulCreature:
    def __init__(self,*args,**kwargs):
        try:
            self.name = kwargs["name"]
        except KeyError:
            print('Please enter the name attribution')
        try:
            self.sp = kwargs["sp"]
        except KeyError:
            print('Please enter the sp attribution.')
        self.attack = random.randint(2,5)
        self.defense = random.randint(2,5)
        self.speed = random.randint(1,4)
    def print_name(self):
        try:
            print(self.name)
        except AttributeError:
            print("No such attribution yet.")

class ManWithSword:
    def __init__(self,name):
        self.name = name

J = FoulCreature(name="Jack",sp="Fireball")

J.print_name()