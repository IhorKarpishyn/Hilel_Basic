'''
Ваша задача — написать программу, которая переводит число во время в читабельном виде.
Пользователь должен ввести число больше 0 и меньше 8639999.
Число необходимо перевести в день, часы, минуты и секунды.
Ну и дополнительной задачей является — забота о выводе.
Слово "день" подбирается на основе кол-ва дней, а часы, минуты и секунды должны заполняться
нулями при одноцифровых значениях.

Пример:
0 -> 0 дней, 00:00:00
224930 -> 2 дня, 14:28:50
466289 -> 5 дней, 09:31:29
8639999 -> 99 дней, 23:59:59
'''

twentyfour_hours = {
    'Day': 86400,
    'Hour': 3600,
    'Minute': 60,
}
day = {
    'день': [1],
    'дня': [2, 3, 4],
    'дней': [0, 5, 6, 7, 8, 9]
}

lifetime = {}

day_time = (int(input("Введите число от 0 до 8639999 : ")))
if day_time in range(0, 8640000):
    for key, value in twentyfour_hours.items():
        lifetime[key] = (day_time // value)
        day_time -= lifetime[key] * value
    lifetime['Second'] = day_time
for key, value in day.items():
    for i in value:
        if lifetime['Day'] % 10 == i:
            dni = key
print(lifetime['Day'], '{dni},'.format(dni=dni), '{:02}'.format(lifetime['Hour']), ':',
      '{:02}'.format(lifetime['Minute']), ':',
      '{:02}'.format(lifetime['Second']))
