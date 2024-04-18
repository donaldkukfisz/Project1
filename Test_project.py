import random


print('Program do zgadywania liczby z zakresu od 1 do 10 000')
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

