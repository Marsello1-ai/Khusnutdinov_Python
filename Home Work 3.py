from array import array

print('\n Напишите слово "Старт", для того, чтобы программа начала работать'
      'или "Стоп" для выхода из нее.')
start = input('Строка ввода: ')

while True:

    if start.lower() == 'старт':


        print('\nНапиште целое число положительное, до которого необходимо сосчитать и вывести все числа крастные 3 ')
        a = (int(input('Строка ввода: ')))

        numbers = array('i', list(range(1, a)))

        for number in numbers:
            if number % 3 == 0:
                print(f' {number}')

    elif start.lower() == 'стоп':
        break

    else:
        print(f'\nВы ввели неправильную команду для старта - {start}')
        break
