class House:
    def __init__(self, NumberOfFloors):
        self.NumberOfFloors = NumberOfFloors

    def say_number(self):
        print(f'Текущий этаж равен {self.NumberOfFloors}')




NumberOfFloors = House(10)
NumberOfFloors.say_number()

