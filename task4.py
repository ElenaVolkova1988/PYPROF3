#Создайте словарь со списком вещей для похода в качестве 
#ключа и их массой в качестве значения. Определите какие 
#вещи влезут в рюкзак передав его максимальную 
#грузоподъёмность. Достаточно вернуть один допустимый вариант.

max_weight=int(input('Введите грузоподъемность:'))
things={'рыболовные снасти': 2, 'топор': 3, 'палатка': 20, 'термос': 1}
for k, v in things.items():
    if v <=  max_weight:
        print(f'В рюкзак влезет : {k}')
        max_weight -= v
    
