'''
Вам необходимо "перевернуть" 5-ти значное число задом наперёд, т.е. чтобы в результате получилось тоже 5-ти значное число, но с обратной последовательностью цифр.
Число ВСЕГДА 5-ти значное и оно не содержит нулей!
Используются только целые числа.
Для решения задачи нужно использовать только тот срез данных, который был пройден. Т.е. использовать строки нельзя.

Примеры:
12345 -> 54321
37568 -> 86573
'''

inverted_number = 0
number = int(input('Enter a five-digit number:'))
inverted_number = inverted_number + int(number) % 10
number /= 10
inverted_number = inverted_number * 10 + int(number) % 10
number /= 10
inverted_number = inverted_number * 10 + int(number) % 10
number /= 10
inverted_number = inverted_number * 10 + int(number) % 10
number /= 10
inverted_number = inverted_number * 10 + int(number) % 10
print(inverted_number)
