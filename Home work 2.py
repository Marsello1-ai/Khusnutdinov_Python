while True:

    print('\nВведите имя "Вячеслав", чтобы получить "Привет, Вячеслав"')
    name = input('Строка ввода: ')
    if name.lower() == "вячеслав":
        print(f'Привет, {name.title()}')
        break
    else:
        print(f'Нет такого имени {name}')
