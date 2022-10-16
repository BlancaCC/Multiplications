#!/usr/bin/python3
from random import choices
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

    init_time = time()
    working_time = 3 * 60 # minutes

    total_time = 10
    numbers = [*list(range(11)), 6,7,7,8,8,9,9,100]
    signs = [-1,-1,1,1]

    while time() < init_time + working_time: 
        r = -111
        a,b = choices(numbers, k=2)
        sa, sb = choices(signs, k=2)
        a = sa*a
        b = b*sb
        expected_value = a*b
        ms = f"""
==============================
    ¿Cuánto es {a} x {b}? 
==============================
Teclea el número y pulsa enter: 
"""
        r = integer_input(ms)
        tries += 1
        while(r != expected_value):
            
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
        print(f'Muy bien Cris :) llevas una precisión de {correct/tries*100}% y te quedan {(init_time + working_time-time())/60 :1.2} min de práctica')
        sleep(0.5)
        clear_terminal()
        print(f'Muy bien Cris :) llevas una precisión de {correct/tries*100}% y te quedan {(init_time + working_time-time())/60 :1.2} min de práctica')
    # Stats
    print('='*10)
    print('Fin del entrenamiento')
    print(f'Precisión: {correct/tries*100}%')
    print(f'Tiempo medio: {(time()-init_time)/correct:1.2} s/multiplicación')



