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
    
    
    

    
