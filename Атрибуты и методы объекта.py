class House:
    def __init__(self, NumberOfFloors):
        self.NumberOfFloors = NumberOfFloors


NumberOfFloors = House(10)
for i in range(1, 11):
    print('Текущий этаж равен', i)
