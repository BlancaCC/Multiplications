#!/usr/bin/python3
from random import choices, shuffle
from time import sleep, time
import os
def clear_terminal():   
    os.system('cls' if os.name == 'nt' else 'clear')
#from  unicodedata import unicode
def integer_input(ms):
    r = 'a'
    while not r.lstrip('-').isdigit():
        r = input(ms)
    return int(r)


if __name__ == '__main__':
    correct  = 0
    tries = 0

    total_operations = 20 

    numbers = [*list(range(11)), 6,7,7,8,8,9,9,100]
    signs = [-1,1]

    products = [
        tuple(choices(numbers, k=2))
        for i in range(total_operations)
    ]
    products_sign = [
        tuple(choices(signs, k=2))
        for i in range(total_operations)
    ]
    

    while products: 
        r = -111
        a,b = products.pop()
        sa, sb = products_sign.pop()
        a = sa*a
        b = b*sb
        expected_value = a*b
        ms = f"""
========================================
        ¿Cuánto es {a} x {b}? 
========================================
teclea el número y pulsa enter: 
"""
        r = integer_input(ms)
        tries += 1
        while(r != expected_value):
            products.append((b,a))
            products_sign.append(tuple(choices(signs, k=2)))
            shuffle(products)
            print("""
            ¡Error! 
    Vuelve a intentarlo""")
            sleep(0.6)
            clear_terminal()
            print("""
            ¡Error! 
    Vuelve a intentarlo""")
            r = integer_input(ms)
            tries += 1
        correct += 1
        clear_terminal()
        print('¡CORRECTO!')
        sleep(0.4)
        print(f'Muy bien Cris :) llevas una precisión de {correct/tries*100}% y te quedan {len(products)} operaciones')
        sleep(0.5)
        clear_terminal()
        print(f'Muy bien Cris :) llevas una precisión de {correct/tries*100}% y te quedan {len(products)} operaciones')
    # Stats
    print('='*85)
    print('Fin del entrenamiento')
    accuracy  = correct/tries*100
    print(f'Precisión: {accuracy}%')
    if(accuracy < 93):
        print(
            '''... Ummm ... 
¿Crees que equivocarse tanto significa saber multiplicar?
VENGA ÁNIMO INTÉNTALO OTRA VEZ
        ''')
    else:
        print('Este resultado está genial Cris, ¡ENHORABUENA!')
    



