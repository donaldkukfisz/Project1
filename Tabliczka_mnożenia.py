print("""
      Tabliczka mnożenia.
      """)

number_one = list(range(0, 11))



    
print(' * |  0  1  2  3  4  5  6  7  8  9  10')
print('---+----------------------------------')
for number in number_one:
    print(f'{number:2} |', end='')
    for i in number_one:
        print(f'{number * i:3}', end='')
    print()
    

    
