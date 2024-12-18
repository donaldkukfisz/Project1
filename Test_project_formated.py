import random
import requests
import json
import time
import pygame
import stars

pygame.init()

def main():   
    print('''Program zawierający kilka funkcjonalnosci będących testem kodu.
          
    Wybierz którą z funkcji chcesz wypróbować:
        
        1) Program do zgadywania liczb z zakresu od 1 do 10 000
        2) Prosty kalkulator
        3) Tabliczka mnożenia
        4) Prognoza pogody w miastach
        5) Gra w poszukiwanie skarbu
        6) Gra z rzutem koscią
        7) Problemy matematyczne
        8) Gra w zbieranie gwiazdek
        
        
    ''')
    
    while True:
        choice = int(input('Który program wydaje się ciekawy? (Wybierz cyfrę od 1 do 8 i potwierdź ENTEREM): '))
        print('')
        
        if choice == 1:
            guess_the_number()
        elif choice == 2:
            calculator()
        elif choice == 3:
            multiply_table()
        elif choice == 4:
            weather_broadcast()
        elif choice == 5:
            treasure_hunting()
        elif choice == 6:
            rolling_dice()
        elif choice == 7:
            mathematic_problems()
        elif choice == 8:
            stars.main()
            
        else:
            print('Nie ma programu o takim numerze! Dokonaj odpowiedniego wyboru z zakresu od 1 do 6:')
            print('')
            continue
             
    input()
            
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
        if guess > 10000:
            print('Liczba poza zakresem!')
        elif guess < number:
            print('Za mało!')
        elif guess > number:
            print('Za dużo!')
        elif guess == number:
            print('Gratulacje, odnalazłeś liczbę!')
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
            x = int(input('Podaj pierwszą liczbę: '))
            y = int(input('Podaj drugą liczbę: '))
            mnozenie = x * y
            print(f'Liczba {x} pomnożona przez {y} wynosi: {mnozenie}')
            print('')

            
        elif number == 4:
            x = int(input('Podaj pierwszą liczbę: '))
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
   
def weather_broadcast():
    
    print('Program do sprawdzania aktualnej pogody w miastach.')
    query = input('W jakim miescie chcesz sprawdzić pogodę?: ')
    
    api_key = 'b5ac8b7f5dd1e0df9b1a5ec9861fec33'
    
    
    response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={query}')
    formated = response.json()
    
    if response.status_code == 200:
        if 'current' in formated:
            current_weather = formated['current']
            temperature = current_weather['temperature']
            feelslike = current_weather['feelslike']
            
            print('')
            print(f'Temperatura w {query} wynosi: {temperature} stopni Celsjusza.')
            print(f'Odczuwalna temperatura w {query} wynosi: {feelslike} stopni Celsjusza.')
            print('')
            
        else:
            print('Błąd, nie można odczytać temperatury. Sprawdź czy poprawnie wpisałes nazwę miasta.')
    
def treasure_hunting():
    
    game_width_x = 20
    game_height_y = 20

    treasure_location_x = random.randint(0, game_width_x)
    treasure_location_y = random.randint(0, game_height_y)

    player_x = 0
    player_y = 0
    
    print('')
    print('')
    print('Wybrałes grę w poszukiwanie skarbu.')
    print('')
    print('Gra odbywa się na obszarze 20 pól na 20 pól. Zacznasz w lewym dolnym rogu z pozycji 0,0.')

    while True:
        choice = input('W którą stronę idziesz? [G, D, L, P]: ')
        
        if choice.lower() == 'g':
            player_y += 1
        elif choice.lower() == 'd':
            player_y -= 1
        elif choice.lower() == 'l':
            player_x -= 1
        elif choice.lower() == 'p':
            player_x += 1
           
        print(f'Szerokosc gracza: {player_x}, wysokosc gracza: {player_y}')
        print('')
        
        if player_x < 0:
            print('Uderzyłes w scianę, spróbuj innego kierunku!')
            player_x = 0
            continue
        if player_y < 0:
            print('Uderzyłes w scianę, spróbuj innego kierunku!')
            player_y = 0
            continue
        
        if player_x == treasure_location_x and player_y == treasure_location_y:
            print('Gratulacje, odnalazłes skarb! Gra zakończona!')
            print(f'Skarb znajdował się na współrzędnych ({player_x}, {player_y})')
            input()
            break
        elif player_x == treasure_location_x:
            print('Jestes w jednej szerokosci ze skarbem!')
            print('')
        elif player_y == treasure_location_y:
            print('Jestes w jednej wysokosci ze skarbem!')
            print('')
            
def rolling_dice():
    
    def roll_dice():
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)
        
        return roll

    print('Zabawa z kostką do gry.')

    while True:
        
        number_of_players = input('Podaj liczbę graczy między 2-5: ')
        
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
        else:
            print('Błąd, nie podałes liczby, spróbuj ponownie.')
            continue
        
        
        if number_of_players < 2 or number_of_players > 5:
            print('Niewłaciwa liczba graczy, spróbuj ponownie.')
            continue
        
        else:
            print(f'Liczba graczy to: {number_of_players}')
            break
        
    max_score = 30

    player_scores = [0 for player in range(number_of_players)]
    #player scores to lista punktów dla każdego zawodnika z number_of_players)




    while max(player_scores) < max_score:
        
        for player in range(number_of_players):
            
            print('')
            print(f'Kolej gracza {player + 1}!')
            
            
            sum_of_points = 0
            
            while sum_of_points < 30:
                
                throw = input('Czy chcesz rzucić kostką? (T): ')
                print('')
                if throw.lower() != 't':
                    break
            
                value = roll_dice()
                if value == 1:
                    print('Wyrzuciłes 1! Twój wynik zostaje wyzerowany!')
                    sum_of_points = 0
                    break
                
                else:
                    print(f'Wyrzuciłes: {value}')
                    sum_of_points += value
                    print(f'Twój obecny wynik to: {sum_of_points}')
                    
            player_scores[player] = sum_of_points
                            
            if player_scores[player] >= max_score:
                print('')
                print('KONIEC GRY')
                print(f'Zwyciężcą jest gracz z numerem {player + 1}!')
                break
            
        
def mathematic_problems():
    
    number_1 = 3
    number_2 = 10

    operators = ['+', '-', '*']

    number_of_questions = 10

    print('Program generujący losowe problemy matematyczne.')
    print('Spróbuj rozwiązać wszystkie 10 poprawnie!')
    print('')



    input('Wcinij enter aby zacząć!')
    print('########################')
    #zaczynamy odliczać czas
    start = time.time()


    def generate_problem():
        
        left_side = random.randint(number_1, number_2)
        right_side = random.randint(number_1, number_2)
        
        problem = str(left_side) + ' ' + random.choice(operators) + ' ' + str(right_side)
        answer = eval(problem)
        
        return problem, answer

    mistakes = 0

    for i in range(number_of_questions):
        
            problem, answer = generate_problem()
            guess = int(input('Problem #' + str(i + 1) + ': ' + problem + ' = '))
            
            if guess == answer:
                print('Prawidłowo! \n')
            
            else:
                print('Błąd! \n')
                mistakes += 1

    #liczymy różnicę od początku do końca by wyznaczyć czas całkowity
    endtime = time.time()
    sum_of_time = endtime - start

    print('########################')
    print('')    
    print(f'Koniec! Popełniłes {mistakes} błędów.')
    print(f'Twój czas to {sum_of_time} sekund.')


    input()
                
                             

    
if __name__ == '__main__':
    main()
    input('Naciśnij ENTER, aby zakończyć...')
    

