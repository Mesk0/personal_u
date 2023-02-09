from random import randint

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        # 返回一个1到6的随机数
        return randint(1, self.num_sides)

