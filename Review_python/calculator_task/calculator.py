def summ(n1, n2):
    print(n1 + n2)


def sub(n1, n2):
    print(n1 - n2)


def mul(n1, n2):
    print(n1 * n2)


def div(n1, n2):
    print(n1 / n2)


operations_dict = {'+': summ, '-': sub, '*': mul, '/': div}


num1 = input('Введите первое число: ')
operation = input('Введите операцию которую хотите выполнить ( +, -, *, /): ')
num2 = input('Введите второе число: ')

if operation in operations_dict:
    if num1.isdigit() and num2.isdigit():
        if int(num2) == 0:
            print('На ноль делить нельзя.')
        else:
            operations_dict[operation](int(num1), int(num2))
    else:
        print('Вероятно Вы ввели букву, введите число.')
else:
    print('Такой операции не существует. Возможные операции:  +, -, *, /')
