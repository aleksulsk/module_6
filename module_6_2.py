class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_owner(self):
        return self.owner

    def get_model(self):
        return self.__model

    def get__color(self):
        return self.__color

    def get__engine_power(self):
        return self.__engine_power

    def get_horsepower(self):
        return (f"Мощность двигателя: {self.get__engine_power()}")

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get__color())
        print(f"Владелец: {self.get_owner()}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()



# Проверяем что поменялось
vehicle1.print_info()
