class car:
    def __init__(self, color, mark, max_speed, weight):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed
        self.weight = weight
    f = 0
    def sound(self):
            print("beep")
            self.f = 1

    def long_sound(self):
        print('beep-beep')



mers = car("Чёрная", "мерседес", 400, 1000)
mers = car('Чёрная', 'мерседес', 400, 1000)
mers.sound()
mers.long_sound()

print(mers.color)
print(mers.mark)
print(mers.max_speed)
print(mers.weight)

