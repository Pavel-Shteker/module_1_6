my_dict = {'Гоголь':1836, 'Грибоедов':1795,
           'Тургенев':1818, 'Достоевский':1821,
           'Горький':1868, 'Тютчев':1803 }
print ('Наш словарь:', my_dict)
print ('Запрошенное значение:', my_dict.get('Достоевский'))
print ('Отсуствующее запрошенное значение:',
       my_dict.get('Сорокин', 'Родился Анисим, да и черт бы с ним'))
my_dict.update({'Блок>': 1880,
                'Лермонтов': 1814})
oblivion = my_dict.pop('Гоголь')
print ('Удаленное значение:', oblivion)
print ('Измененный словарь:', my_dict)

my_set = {1, 1, -3.42, -3.42, "WOW", "WOW", False}
print ('Множество:', my_set)
my_set.add(len(str(my_dict)))
my_set.add(2**4)
my_set.discard(1)
print ('Измененное множество:', my_set)

