import random

print('''Program zawierający kilka funkcjonalnosci będących testem kodu.
      
Wybierz którą z funkcji chcesz wypróbować:
    
    1) Program do zgadywania liczb z zakresu od 1 do 10 000
    2) Prosty kalkulator
    
''')

while True:
    choice = int(input('Który program wydaje się ciekawy? '))
    
    if choice == 1:
        print('')
        print('''Program do zgadywania liczby z zakresu od 1 do 10 000. 
    Liczba została już dla Ciebie wybrana, spróbuj ją odgadnąć!''')
        print('...')
    
        number = random.randint(1, 10000)
    
        while True:
            liczba = int(input('Podaj liczbę: '))
            if liczba > number:
                print('Za dużo!')
            elif liczba < number:
                print('Za mało!')
            elif liczba > 10000:
                print('Liczba poza zakresem!')
            elif liczba == number:
                print('Gratulacje, odnalazłes liczbę!')
                input()
                break
    input()
    
    if choice == 2:
        print('')
        print(''' Wybrałes prosty kalkulator działań na dwóch liczbach. Możliwe jest:
              
              1) dodawanie,
              2) odejmowanie, 
              3) mnożenie 
              4) dzielenie.''')
        print('')
        number = int(input('Która z opcji Cie interesuje? '))
        if number == 1:
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            suma = x + y
            print(f'Suma liczb wynosi: {suma}')
            
        elif number == 2:
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            różnica = x - y
            print(f'Różnica liczb wynosi: {różnica}')
            
        elif number == 3:
            x = x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            mnozenie = x * y
            print(f'Liczba {x} pomnożona przez {y} wynosi: {mnozenie}')
            
        elif number == 4:
            x = x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            dzielenie = x / y
            print(f'Liczba {x} podzielona przez {y} wynosi: {dzielenie}')
            
    
    
        
    input()

