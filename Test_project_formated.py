import random

def main():   
    print('''Program zawierający kilka funkcjonalnosci będących testem kodu.
          
    Wybierz którą z funkcji chcesz wypróbować:
        
        1) Program do zgadywania liczb z zakresu od 1 do 10 000
        2) Prosty kalkulator
        3) Tabliczka mnożenia
        
    ''')
    
    while True:
        choice = int(input('Który program wydaje się ciekawy? (Wybierz cyfrę od 1 do 3 i potwierdź ENTEREM): '))
        
        if choice == 1:
            guess_the_number()
        elif choice == 2:
            calculator()
        elif choice == 3:
            multiply_table()            
            
def guess_the_number():
    
    print('')
    print('''
Program do zgadywania liczby z zakresu od 1 do 10 000. 
Liczba została już dla Ciebie wybrana, spróbuj ją odgadnąć!
    ''')
    print('...')
        
    number = random.randint(1, 10000)
        
    while True:
        guess = int(input('Podaj liczbę: '))
        if guess > number:
            print('Za dużo!')
        elif guess < number:
            print('Za mało!')
        elif guess > 10000:
            print('Liczba poza zakresem!')
        elif guess == number:
            print('Gratulacje, odnalazłes liczbę!')
            input()
                    
def calculator():
    
    print('')
    print(''' 
Wybrałes prosty kalkulator działań na dwóch liczbach. Możliwe jest:
          
1) dodawanie,
2) odejmowanie, 
3) mnożenie 
4) dzielenie.''')
    print('')
    
    while True:
        number = int(input('\nKtóra z opcji kalkulatora Cie interesuje? '))
        
        if number == 1:
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            suma = x + y
            print(f'Suma liczb wynosi: {suma}')
            print('')

            
        elif number == 2:
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            różnica = x - y
            print(f'Różnica liczb wynosi: {różnica}')
            print('')

            
        elif number == 3:
            x = x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            mnozenie = x * y
            print(f'Liczba {x} pomnożona przez {y} wynosi: {mnozenie}')
            print('')

            
        elif number == 4:
            x = x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            dzielenie = x / y
            print(f'Liczba {x} podzielona przez {y} wynosi: {dzielenie}\n')
            print('')

            
        moving_on = input('Czy chcesz kontynuować działanie programu? T/N: ')
        if moving_on.lower() == 't':
            continue
        elif moving_on.lower() == 'n':
            break
                
def multiply_table():
    
    print('')
    print('Oto tabliczka mnożenia do 10.')
    print('')

    number_one = list(range(0, 11))



        
    print(' * |  0  1  2  3  4  5  6  7  8  9  10')
    print('---+----------------------------------')
    for number in number_one:
        print(f'{number:2} |', end='')
        for i in number_one:
            print(f'{number * i:3}', end='')
        print()
    
    print('')
    moving_on = input('Czy chcesz sprawdzić inny program? T/N: ')
    if moving_on.lower() == 't':
        main()
    elif moving_on.lower() == 'n':
        print('')
        print('-' * 40)
        print('Dziękujemy za skorzystanie z programu!')
        print('-' * 40)
        input()
        quit()
   
                
                               

    
if __name__ == '__main__':
    main()
    
