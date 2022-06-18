'''
Вам необходимо "перевернуть" 5-ти значное число задом наперёд, т.е. чтобы в результате получилось тоже 5-ти значное число, но с обратной последовательностью цифр.
Число ВСЕГДА 5-ти значное и оно не содержит нулей!
Используются только целые числа.
Для решения задачи нужно использовать только тот срез данных, который был пройден. Т.е. использовать строки нельзя.

Примеры:
12345 -> 54321
37568 -> 86573
'''

number = int(input('Enter a five-digit number:'))
inverted_number = 0
if 9999 < number < 100000:
    for i in str(number):
        if int(i) == 0:
            print("Number contains zero! Bye!!!")
            inverted_number = 0
            break
        else:
            inverted_number = inverted_number * 10 + int(number) % 10
            number /= 10
    if inverted_number != 0:
        print(inverted_number)
else:
    print('Number must be five digits. Bye!')
