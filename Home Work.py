while True:
    print('\nВведите любое целое число больше "7", чтобы получить "Привет".')

    number = int(input('Строка ввода: '))
    if number > 7 :
        print('Привет')
        break
    else:
        print(f'Вы ввели число {number}')