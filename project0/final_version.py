"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
from game_v2 import score_game, random_predict
import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Угадываем число с помощью алгоритма

        Args:
            number (int, optional): Загаданное число. Defaults to 1.

        Returns:
            int: Число попыток
        """
    min_number = 0 
    max_number = 101
    count = 0
    prediction = 50
    while True:
        count += 1
        if number != prediction:
            if number > prediction:
                min_number = prediction
                prediction = round(np.mean([prediction, max_number]))
            if number < prediction:
                max_number = prediction
                prediction = round(np.mean([min_number, prediction]))
        if number == prediction:
            break # выходим из цикла если число угадано
    return count
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)