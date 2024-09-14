"""Igra Ugadai chislo. Computer guess number itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Count of attempt
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 500) # predict number
        if predict_number == number:
            break
    
    return count


def score_game(random_predict) -> int:
    """Za kakoe colichestvo popitok v srednem iz 1000 podhodov ugadivaet nash algoritm

    Args:
        random_predict (_type_): Funtion ugadivania

    Returns:
        int: srednee colichestvo popitok
    """
    
    count_ls = [] # list of attempt count
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # mean of attempts
    
    print(f'Your algorithm guess mean for: {score} attempts')
    return score

if __name__ == '__main__':
    # RUN
    score_game(random_predict)