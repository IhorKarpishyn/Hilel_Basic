'''
На вход функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда
начиналось с большой буквы и заканчивалось точкой.
Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку,
то добавлять еще одну не нужно, это будет ошибкой
Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).
Пример:
correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."
'''


def correct_sentence(work_string):
    final_string = ''
    if len(work_string) > 0:
        if work_string[len(work_string) - 1] != '.':
            work_string += '.'
        if work_string[0].upper() != work_string[0]:
            first_letter = work_string[:1]
            first_letter = first_letter.capitalize()
            final_string = first_letter + work_string[1:]
        else:
            final_string += work_string
    return final_string


user_string = input('Введите предложение : ')
output = correct_sentence(user_string)
print('Исправленное предложение : ', output)

