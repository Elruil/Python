
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
# num = list_1[0]
# separate = abs(list_1[0] - k)
# for i in range (0, len(list_1)):
#     if abs(list_1[i] - k) < separate:
#         num = list_1[i]
#         separate = abs(list_1[i] - k)
# print(num)            

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#     ● A, E, I, O, U, L, N, S, T, R – 1 очко; 
#     ● D, G – 2 очка;
#     ● B, C, M, P – 3 очка;
#     ● F, H, V, W, Y – 4 очка; 
#     ● K – 5 очков; 
#     ● J, X – 8 очков; 
#     ● Q, Z – 10 очков.
#     А русские буквы оцениваются так: 
#  ● А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#  ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка; 
#  ● Й, Ы – 4 очка; ● Ж, З, Х, Ц, Ч – 5 очков; 
# ● Ш, Э, Ю – 8 очков;
#   ● Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#   Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
#   либо только русские буквы.
d = dict()
d["AEIOULNSTRАВЕИНОРСТ"] = 1
d["DGДКЛМПУ"] = 2
d["BCMPБГЁЬЯ"] = 3
d["FHVWYЙЫ" ] = 4
d["KЖЗХЦЧ"] = 5
d["JXШЭЮ"] = 8
d["QZФЩЪ"] = 10


word = input("Введите слоо для оценки:  ")
print(word)
result = 0
for letter in word:
    for key, value in d.items():
        if letter.upper() in key:
            result += value
print(result)        
    
    
    
