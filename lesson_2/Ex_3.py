'''
Пользователь вводит 4-хзначное число с клавиатуры. Написать программу, которая выводит цифры, из которого это число состоит. Например пользователь вводит 1234, а программа выводит:
1
2
3
4
Задачу необходимо решить используя методы деления (подсказка // и % или divmod).
Число ВСЕГДА 4-хзначное!
'''


number = int(input('Enter a four-digit number:'))
print(number // 1000)
number %= 1000
print(number // 100)
number %= 100
print(number // 10)
number %= 10
print(number)

