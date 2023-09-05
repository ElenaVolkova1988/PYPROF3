#Дан список повторяющихся элементов. Вернуть список 
#с дублирующимися элементами. В результирующем списке 
#не должно быть дубликатов

my_list = [1,2,3,1,2,3,6,9,8]
double=[]
new_list=[]

for item in my_list:
    if my_list.count(item) > 1 and item not in double:
        double.append(item)
    else:
        new_list.append(item)

print(f' Список с дублирующими элементами : ', double)
print(f' Список без  дубликатов : ', new_list)

        