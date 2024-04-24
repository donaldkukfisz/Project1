import random

print('''Program zawierający kilka funkcjonalnosci będących testem kodu.
      
Wybierz którą z funkcji chcesz wypróbować:
    
    1) Program do zgadywania liczb z zakresu od 1 do 10 000
    
''')
choice = int(input('Który program wydaje się ciekawy?'))

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

