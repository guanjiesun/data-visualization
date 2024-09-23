from random import randint


class Die:
    """骰子的英文，单数是die，复数是dice"""

    def __init__(self, num_sides=6):
        """假设骰子有六面"""
        self.num_sides = num_sides

    def roll(self):
        """返回[1, 6]之间的一个整数"""
        return randint(1, self.num_sides)
