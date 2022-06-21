'''
Ваша программа должна перенести последний элемент списка из конца в начало, т.е. последний элемент списка должен стать первым.
При этом последовательность других элементов не должна меняться.
Пустой список или список только с одним элементом должен остаться прежними
[12, 3, 4, 10] => [10, 12, 3, 4]
[1] => [1]
[] => []
'''

start_list = [12, 3, 4, 10]
#Пустой список или список только с одним элементом должен остаться прежними
if len(start_list) > 1:
    last_item_list = [start_list[len(start_list)-1]]
    del(start_list[len(start_list)-1])
    start_list = last_item_list + start_list
print(start_list)
