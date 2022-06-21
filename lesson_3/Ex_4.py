'''
Программа должна выполнять простые математические действия. Пользователю предлагается
ввести числа и действие над этими числами, а программа, исходя из действия, вычисляет и печатает результат.
Сделать проверку на то, что при делении, делитель не равен 0!
'''

x = float(input('Введите первое число: '))
y = float(input('Введите второе число : '))
if y == 0:
    operator = input('Выберите оператор из предложенных (только + , - , * ) ')
else:
    operator = input('Выберите оператор из предложенных (+ , - , * , / ) ')
result = None
if operator == '+':
    result = x+y
elif operator == '-':
    result = x-y
elif operator == '*':
    result = x*y
elif operator == '/':
    if y != 0:
        result = x/y
    else:
        print('Вы все таки ввели /  Делить на ноль нельзя!!!!')
else:
    print('Вы ввели неверный оператор')
if result!= None:
    if result.is_integer():
        result = int(result)
    print(result)

