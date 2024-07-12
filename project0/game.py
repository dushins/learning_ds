import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    prediction = int(input('Угадайте число '))
    count += 1
    
    if number < prediction:
        print('число должно быть меньше')
        
    elif number > prediction:
        print('число должно быть больше')
        
    else:
        print(f'вы угадали! это число {number}, вы потратили {count} попыток')
        break