import random

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
        
    
    
        
        
        
    
        
    

   

    
       
        

    
    

