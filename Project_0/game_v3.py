#test of git

import numpy as np


def golden_ratio_predict(number:int=1) -> int:   # Улучшенный алгоритма
    '''Сначала устанавливаем число 64, а потом уменьшаем или увеличиваем его по правилу золотого сечения.
       Функция принимает загаданное число и возвращает число попыток'''

    count = 1
    predict = 64    # начальное предполагаемое числ
    high_limit = 101
    low_limit = 1

    while number != predict:
        count+=1
        if number > predict:
            low_limit = predict
        else:
            high_limit = predict
        predict = int((high_limit-low_limit)/2+low_limit)   # вычисление нового среднего

    return(count) # выход из цикла, если угадали


def score_game(type_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(type_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#if __name__ == '__main__':
# RUN
score_game(golden_ratio_predict)