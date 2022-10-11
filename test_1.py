from functools import wraps
from time import sleep
import random
"""
для демонстрации задания делаем ф-цию, которая из лут листа будет случайно выбирать лут и еще 1 ф-цию, которая будет  показывать список всего возможного лута
"""
loot_list = ['gold', 'item', 'weapon']


def wait(n):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'There was a pause {n} seconds before execution {func.__name__}')
            sleep(n)
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@wait(3)
def loot_choise(some_list):
    loot = random.choice(some_list)
    return loot

print(loot_choise(loot_list))