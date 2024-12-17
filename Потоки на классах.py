from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_left = 100
        self.days = 0


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies_left > 0:
            sleep(1)
            self.days += 1
            self.enemies_left -= self.power

            if self.enemies_left < 0:
                self.enemies_left = 0
            print(f'{self.name} сражается {self.days} дней,  осталось{self.enemies_left} воинов.\n')
        print(f'{self.name} одержал победу спустя {self.days} дней!')
f1_knight = Knight('Sir Lancelot', 10)
f2_knight = Knight('Sir Galahad', 20)

f1_knight.start()
f2_knight.start()
f1_knight.join()
f2_knight.join()

print('Все битвы закончились!')
