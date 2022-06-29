'''
Дописать калькулятор таким образом, чтобы он работал до тех пор, пока пользователь этого хочет
Т.е. нужно делать запрос у пользователя на продолжение работы калькулятора после каждого вычисления - если пользователь
ввел yes ( можно просто y), то новое вычисление, в противном случае - окончание работы.
'''

is_working = True
while is_working is True:
    x = float(input('Введите первое число : '))
    y = float(input('Введите второе число : '))
    if y == 0:
        operator = input('Выберите оператор из предложенных (только + , - , * ) ')
    else:
        operator = input('Выберите оператор из предложенных (+ , - , * , / ) ')
    result = None
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        if y != 0:
            result = x / y
        else:
            print('-' * 80)
            print("Вы все таки ввели / . Делить на ноль нельзя!!!!")
            print('Начнем заново!!!')
            print('-' * 80)
    else:
        print('-' * 80)
        print('Вы ввели неверный оператор')
        print('Начнем заново!!!')
        print('-' * 80)
    if result is not None:
        if result.is_integer():
            result = int(result)
        print('Ответ : ', result)
    print('-' * 80)
    will_work = input("Вы желаете продолжить вычисления?  Чтобы продолжить введите - 'yes' или 'y' ")
    print('-' * 80)
    if will_work.lower() != 'yes' and will_work.lower() != 'y':
        is_working = False
        print('Bye!!!')
        print('-' * 80)
