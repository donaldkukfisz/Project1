import random

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