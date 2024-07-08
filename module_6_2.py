class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, model:str, color:str, engine_power:int):
        self.owner = owner  # владелец транспорта. (владелец может меняться)
        self.__model = model  # модель (марка) транспорта
        self.__engine_power = engine_power  # мощность двигателя.
        self.__color = color
        self.__color_variants = self.__COLOR_VARIANTS
    def get_model(self, model):   # Модель
        return (f'Модель: {self.__model}')

    def get_horsepower(self, model):      #Мощность
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, color):      #Цвет
       return (f'Цвет: {self.__color}')

    def print_info(self):
        print(f'{self.get_model(self)}'
              f'\n{self.get_horsepower(self)}'
              f'\n{self.get_color(self)}'
              f'\nВладелец: {self.owner}')

    def set_color(self, search_color:str):
        search_color_lower = search_color.lower()
        if search_color_lower in self.__color_variants:
            self.__color = search_color
        else:
            print(f"Невозможно покрасить в {search_color}")


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

    

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

#Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
