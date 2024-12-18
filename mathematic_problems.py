import random
import time

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
            
        
        
        
        
    






    


    