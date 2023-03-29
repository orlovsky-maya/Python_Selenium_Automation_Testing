num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))


try:
    print(f'Результат: {num1 // num2}')
except ZeroDivisionError:
    print('На ноль делить нельзя')

