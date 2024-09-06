class Horse:
    '''класс описывающий лошадь'''

    # Если не пользоваться super()
    #def __init__(self, x_distance=0, sound='Frrr'):

    def __init__(self, *, x_distance=0, sound='Frrr', **kwargs):
        self.x_distance = x_distance  # пройденный путь
        self.sound = sound  # звук, который издаёт лошадь

        super().__init__(**kwargs)  # для Eagle через MRO

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    '''класс описывающий орла'''

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance  # высота полёта
        self.sound = sound  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    '''класс описывающий пегаса'''

    # Марк Лутц в книге «Изучаем Python» советует не использовать super(),
    # а пользоваться явным указанием суперкласса
    #def __init__(self, x_distance=0, y_distance=0, sound='Neigh-neigh!'):
    #    Horse.__init__(self, x_distance, sound)
    #    Eagle.__init__(self, y_distance, sound)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        '''текущее положение пегаса'''
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
