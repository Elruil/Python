
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random
list_1 = list()
count = 0
for i in range(int(input("введите число:  "))):
    list_1.append(random.randint(1,10))
print(*list_1)
num = int(input("Ведите число "))
for i in range(len(list_1)):
    if list_1[i] == num:
        count += 1

print(f"число {num} в списке {list_1} встречается {count} раз") 

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai .
# Последняя строка содержит число X     

import random
list_2 = list()
for i in range(1, (int(input("введите число:  "))) + 1):
    list_2.append(i)
print(*list_2)
num1 = int(input("Ведите число "))
num_old = num1
print(num1)
count = 0
max_count = list_2[len(list_2) - 1] - 1
result = 0
for i in range(len(list_2)):
    num1 = num_old
    while num1 != list_2[i]:        
        if num1 > list_2[i]:
            num1-= 1       
            
        elif num1 < list_2[i]:
            num1 += 1
        count +=1
            
    if count < max_count: 
        max_count = count         
        result = list_2[i]       
    count = 0  
print(result)                   
            

