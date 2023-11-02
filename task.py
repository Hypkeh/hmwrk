class Device:
    def __init__(self, name, functions):
        self.name = name
        self.func = functions

class CoffeMachine(Device):
    def __init__(self, types_of_coffee):
        super().__init__(self.name, self.func)
        self.coffee = types_of_coffee

    def make_coffee():
        return "Кофе готовится"

class Blender(Device):
    def __init__(self, amount_of_speeds):
        super().__init__(self.name, self.func)
        self.speeds = amount_of_speeds

    def do_smoothie():
        return "Пища измельчается"


class MeatGrinder(Device):
    def __init__(self, power):
        super().__init__(self.name, self.func)
        self.power = power

    def grind_meat():
        return "Молотим мясо"




class Ship:
    def __init__(self, name):
        self.name = name

class Supmarine(Ship):
    def __init__(self, depth):
        super().__init__(self.name)
        self.depth = depth

class Cruiser(Ship):
    def __init__(self, capacity):
        super().__init__(self.name)
        self.capacity = capacity


        