import math as m
print('============== Zadanie 1 ==============')
# 1. Продолжаем работать с формулами.
# Используя модуль math, вычислите значения по следующим
# формулам:
x = float(input("Введите значение: x\n"))
n = int(input("Введите количество итераций: n\n"))
# x, n = 6.3, 11

result_for = 0
for i in range(n):
    result_for += pow(-1, i) * pow(x, 2 * i + 1) / m.factorial(2 * i + 1)
result_math = m.sin(x)
error = abs(100 - result_for * 100 / result_math)
print(f'Результат вычисление sin({x}) двумя способами:\n'
      f'через цикл for: {result_for:.6f}\n'
      f'через функцию sin(x) модуля math: {result_math:.6f}\n'
      f'при количестве итераций {n} погрешность составляет: {error} %\n')

print('============== Zadanie 2 ==============')
# 2. Маша хочет накопить на телефон, который стоит N денег. Маша может откладывать k рублей
# каждый день, кроме воскресенья (в воскресенье она тратит эти деньги на поход в
# кино). Маша начинает копить в понедельник. За сколько дней она накопит нужную сумму?
N = float(input("Введите стоимость телефона: N = "))
k = float(input("Введите сумму, откладываемую каждый день: k = "))
# N, k = 700, 100
days = 0
summ = 0
while summ < N:
    days += 1
    if days % 7 != 0:
        summ += k
print(f'Маша накопит на телефон за {days} дней\n')

print('============== Zadanie 3 ==============')
# 3. Реализовать вывод последовательности чисел Фибоначчи
# (1 1 2 3 5 8 13 21 34 55 89 ...), где каждое следующее число
# является суммой двух предыдущих
n = int(input("Сколько чисел Фибоначчи нужно вывести: n = "))
# n = 10
fibo1 = 0
fibo2 = 1
print(fibo2, end=' ')
for i in range(n-1):
    fibo3 = fibo1 + fibo2
    print(fibo3, end=' ')
    fibo1 = fibo2
    fibo2 = fibo3
print()
print()

print('============== Zadanie 4 ==============')
# 4. Дан список чисел. Реализовать программу, которая
# посчитает сумму всех чисел в списке, а также найдет
# минимальный и максимальный элементы.
spisok = [100, 1, 2, 3, 4, 5, 50, 6, 7, 8, 9, 10]
l = len(spisok)
summ = 0
for i in range(l):
    summ += spisok[i]
minn = min(spisok)
maxx = max(spisok)
print(f'Дан список:\n{spisok}\nв списке {l} элементов')
print(f'сумма: {summ}\nминимальное значение: {minn}\nмаксимальное значение: {maxx}\n')

print('============== Zadanie 5 ==============')
# 5. Дан список чисел. Реализовать программу, которая проверит, все ли числа в списке уникальны (встречаются
# только один раз). Программа должна вывести результат проверки, и, если не все элементы уникальны, вывести
# дублирующиеся элементы и количество их повторений в списке
spisok = [100, 1, 2, 10, 7, 3, 10, 4, 5, 50, 6, 100, 7, 8, 9, 10]  # список с повторениями
# spisok = [1, 2, 3, 4, 5, 50, 6, 100, 7, 8, 9, 10]  # список без повторений
l = len(spisok)
spisok_dubl = []
print(f'Дан список:\n{spisok}\nв списке {l} элементов')
print('Дублирующиеся элементы:')
for i in range(l):
    if spisok[i] in spisok_dubl:
        continue
    else:
        dubl = spisok[i]
        count = 1
    for j in range(i+1, l):
        if dubl == spisok[j]:
            count += 1
    if count >= 2:
        spisok_dubl.append(dubl)
        print(f'Элемент {dubl} встречается в списке {count} раз')
if len(spisok_dubl) == 0:
    print('отсутствуют')
print()

print('============== Zadanie 6 ==============')
# 6. Дан список чисел, отсортированных по возрастанию. На вход принимается значение, равное одному из элементов
# списка. Реализовать алгоритм бинарного поиска, на выходе программа должна вывести позицию искомого элемента в
# исходном списке.
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 49, 50, 88, 100, 217]
l = len(spisok)
print(f'Дан список:\n{spisok}\nв списке {l} элементов')
elem = float(input("Номер какого элемента нужно найти: "))
# elem = 9
if elem in spisok:
    i = 0
    while i < l:
        if elem == spisok[i]:
            print(f'Искомый элемент {elem} имеет позицию {i + 1} (нумерация с 1)')
            break
        else:
            i += 1
else:
    print(f'Элемента {elem} нет в списке')
print()

print('============== Zadanie 7 ==============')
# 7*. Реализовать алгоритм бинарного поиска по
# сдвинутому списку отсортированных чисел (например, дан
# список [5, 6, 7, 1, 2, 3, 4])
spisok = [5, 6, 7, 1, 2, 3, 4]
l = len(spisok)
print(f'Дан список:\n{spisok}\nв списке {l} элементов')
elem = float(input("Номер какого элемента нужно найти: "))
max1 = spisok[0]
# min2 = max2 = spisok[l - 1]
last = spisok[1]
last_id = 1
first_id = 1
elem_id_temp = -1
elem_id = -1
if elem in spisok:
    # ищем перелом списка
    # в переменную last запишем максимальное значение 1-й части списка
    # в переменную last_id - индекс этого значения
    i = 0
    while max1 < last:
        if max1 < last:
            i += 1
            max1 = spisok[i]
            last = spisok[i + 1]
    last = spisok[i]
    last_id = i
    # составляем временный список spisok_temp отсортированный по возрастанию
    spisok_temp = []
    len1 = last_id + 1
    len2 = l - last_id - 1
    first_id = last_id + 1
    for i in range(first_id, l):
        spisok_temp.append(spisok[i])
    for i in range(last_id + 1):
        spisok_temp.append(spisok[i])
    # теперь запускаем бинарный поиск
    mid = l // 2
    low = 0
    high = l - 1
    while spisok_temp[mid] != elem and low <= high:
        if elem > spisok_temp[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    # if low > high:
    #     print("Нет значения")
    # else:
    #     print("ID =", mid)
    elem_id_temp = mid
    # вычисляем ID искомого элемента в исходном списке
    if elem_id_temp + 1 > len2:
        elem_id = elem_id_temp + 1 - len2
    else:
        elem_id = elem_id_temp + 1 + len1
    print(f'Искомый элемент {elem} имеет позицию {elem_id} (нумерация с 1)\n')
    print(f'временный список:\n{spisok_temp}')
    # print('elem_id_temp =', elem_id_temp, ' (нумерация с 0)')
else:
    print(f'Элемента {elem} нет в списке')
print()
