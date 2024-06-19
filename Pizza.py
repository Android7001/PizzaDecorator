
class Pizza: #Componente
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Massa(Pizza): #Componente Concreto
    cost = 10

class Decorator(Pizza): #Decorador
    def __init__(self, pizza):
        self.component = pizza

    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + Pizza.getDescription(self)

class Pepperoni(Decorator): #Decorador Concreto 1
    cost = 15
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Mussarela(Decorator): #Decorador Concreto 2
    cost = 6
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Calabresa(Decorator):  # Decorador Concreto 3
    cost = 12
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Frango(Decorator):  # Decorador Concreto 4
    cost = 15
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Catupiry(Decorator):  # Decorador Concreto 5
    cost = 10
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Gorgonzola(Decorator):  # Decorador Concreto 6
    cost = 12
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Parmesao(Decorator):  # Decorador Concreto 7
    cost = 12
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Chocolate(Decorator):  # Decorador Concreto 8
    cost = 16
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Banana(Decorator):  # Decorador Concreto 9
    cost = 8
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

PizzaDeCalabresa = Mussarela(Calabresa(Massa()))
print(PizzaDeCalabresa.getDescription() + ": $" + str(PizzaDeCalabresa.getTotalCost()))

PizzaDoce = Banana(Chocolate(Massa()))
print(PizzaDoce.getDescription() + ": $" + str(PizzaDoce.getTotalCost()))