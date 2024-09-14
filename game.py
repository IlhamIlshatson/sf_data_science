"""Igra Ugadai chislo"""

import numpy as np

number = np.random.randint(1, 101) # guess the number

count = 0 # count of attempt

while True:
    count += 1
    predict_number = int(input('Quess the number from 1 to 100: '))
    
    if predict_number > number:
        print('the number should be less')
    
    elif predict_number < number:
        print('the number should be higher')
        
    else:
        print(f'You guessed the number! This number is = {number}, for {count} attempt')
        break # end of cycle