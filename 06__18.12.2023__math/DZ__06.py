import random

print('===================== Zadanie 1 =====================')
'''
1. Дан список чисел, отсортированных по возрастанию. На
вход принимается значение, равное одному из элементов
TeachMeSkills.by
списка. Реализовать функцию, выполняющую рекурсивный
алгоритм бинарного поиска, на выходе программа должна
вывести позицию искомого элемента в исходном списке
'''
'''
def bin_search(spisok, idx0, idxn, val):

    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
# Compare the search item with middle most value

        if spisok[midval] > val:
            return bin_search(spisok, idx0, midval-1,val)
        elif spisok[midval] < val:
            return bin_search(spisok, midval+1, idxn, val)
        else:
            return midval

spisok = [3,11,14,27,52,88,131,256,318]
l = len(spisok)
print(f'Дан список:\n{spisok}\nв списке {l} элементов')
elem = float(input("Индекс какого элемента нужно найти: "))
print(f'Элемент {elem} имеет индекс {bin_search(spisok, 0, l-1, elem)}')
'''

print('===================== Zadanie 2 =====================')
print('Перевод чиста из десятичной в двоичную систему счисления')
'''
2. Программа получает на вход число в десятичной
системе счисления. Реализовать функцию, которая
переводит входное число в двоичную систему счисления.
Допускается реализация функции как в рекурсивном
варианте, так и с итеративным подходом.
'''
'''
def dec_to_bin(dec: int) -> str:
    b = ''
    while dec > 0:
        b = str(dec % 2) + b
        dec = dec // 2
    return(b)
elem = int(input("Введите десятичное целое число: "))
print(f'В двоичном виде будет: {dec_to_bin(elem)}')
'''

print('===================== Zadanie 3 =====================')
print('Проверка числа на простоту')
'''
3. Программа получает на вход число. Реализовать
функцию, которая определяет, является ли это число простым
(делится только на единицу и на само себя).
'''
'''
def is_prostoe(val):
    k = 0
    for i in range(2, val // 2 + 1):
        if (val % i == 0):
            k = k + 1
    if (k <= 0):
        print(f"Число {val} простое")
    else:
        print(f"Число {val} не является простым")

elem = int(input("Введите целое число: "))
is_prostoe(elem)
'''

print('===================== Zadanie 4 =====================')
print('Наибольший общий делитель')
'''
4. Программа получает на вход два числа и находит их
НОД (наибольший общий делитель). Пример: на вход
подаются числа 12 и 18, их НОД равен 6.
'''
'''
def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return(a + b)

x = int(input("Введите 1-е целое число: "))
y = int(input("Введите 2-е целое число: "))
print(f'Наибольший общий делитель {nod(x, y)}')
'''


print('===================== Zadanie 5 =====================')
print('шифр Цезаря без алфавита, использую сдвиг в кодировочной таблице')
'''
5. Программа получает на вход строку – сообщение и указание, что нужно сделать:
шифровать или дешифровать. Реализовать две функции: первая шифрует заданное
сообщение шифром Цезаря, вторая расшифровывает. В зависимости от выбора
пользователя (шифровать или дешифровать) вызывается соответствующая функция,
результат выводится в консоль.

Для примера можно взять строки
Мама мыла раму
Сесе%сѐре%хесш
'''
'''
key = 5
def codirovanie(text) -> str:
    new_str = ''
    for i in text:
        new_str += chr(ord(i) + key)
    return new_str

def decodirovanie(text) -> str:
    new_str = ''
    for i in text:
        new_str += chr(ord(i) - key)
    return new_str

stroka = str(input("Введите строку для кодирования: "))
decision = int(input("1 - шифровать, 2 -дешифровать\nсделайте выбор (1/2): "))
if decision == 1:
    result = codirovanie(stroka)
    print(f'Зашифрованная строка с ключём {key}:\n{result}')
elif decision ==2:
    result = decodirovanie(stroka)
    print(f'Расшифрованная строка с ключём {key}:\n{result}')
else:
    print('Вы сделали неправильный выбор')
'''

print('===================== Zadanie 6 =====================')
print('шифр Виженера')
'''
6*. См. предыдущую задачу, но вместо шифра Цезаря
использовать шифр Виженера.
'''


print('===================== Zadanie 7 =====================')
print('заполнение матрицы MxN')
'''
7. Реализовать функцию, которая создаёт матрицу
размером M строк на N столбцов и заполняет её рандомными
числами.
'''
def create_matrix(m: int, n: int):
    list_1 = []
    for i in range(0, m):
        temp = []
        for j in range(0, n):
            random_value = random.randint(10, 99)
            temp.append(random_value)
            print(random_value, end=' ')
        list_1.append(temp)
        print()
    return list_1


# M = int(input("Введите размеры матрицы MxN\nM:"))
# N = int(input("Введите размеры матрицы MxN\nN:"))
M = 3
N = 15

matrix = create_matrix(M, N)

print('===================== Zadanie 8 =====================')
print('поиск минимального и максимального элементов в матрице MxN\nиз предыдущей задачи')
'''
8. Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести
в консоль индексы найденных элементов.
'''
'''
def min_max(list_1):
    min = max = list_1[0][0]
    id_min_m = id_min_n = id_max_m = id_max_n = 0
    for i in range(0, M):
        for j in range(0, N):
            if min > list_1[i][j]:
                min = list_1[i][j]
                id_min_m = i
                id_min_n = j
            if max < list_1[i][j]:
                max = list_1[i][j]
                id_max_m = i
                id_max_n = j
    print(f'Минимальное значение {min} с индексами {id_min_m, id_min_n}')
    print(f'Максимальное значение {max} с индексами {id_max_m, id_max_n}')

min_max(matrix)
'''

print('===================== Zadanie 9 =====================')
print('Сумма элементов матрицы, процент столбца в общей сумме матрицы MxN\nиз предыдущей задачи')
'''
9. Реализовать функцию, которая находит сумму
элементов матрицы (матрица M x N). Определить, какую долю
в общей сумме (процент) составляет сумма элементов
каждого столбца.
'''
'''
def sum_matrix(list_1, m, n):
    summ = 0
    for i in range(0, m):
        for j in range(0, n):
            summ += list_1[i][j]
    return summ


def persent_col_matrix(list_1, m, n, s):
    summ_col = []
    percent_col = []
    for i in range(0, n):
        summ = 0
        for j in range(0, m):
            summ += list_1[j][i]
        summ_col.append(summ)
        percent_col.append(round((100 * summ) / s, 1))
    return summ_col, percent_col

sum_m = sum_matrix(matrix, M, N)
sum_col, perc_col =  persent_col_matrix(matrix, M, N, sum_m)
print(f'Сумма элементов матрицы: {sum_m}')
print((f"Суммы столбцов:\n{sum_col}"))
print((f"Процент суммы столбцов в общей сумме:\n{perc_col}"))
'''

print('===================== Zadanie 10 =====================')
print('Перемножение элементов на столбец \'k\' в матрице MxN\nиз предыдущей задачи\n')
'''
10*. Реализовать функцию, которая перемножает
элементы каждого столбца матрицы с соответствующими
элементами K-го столбца (матрица M x N).
'''
'''
print(f"Введите номер K-го столбца, на элементы которого будем умножать все столбцы,"
      f"\nон должен быть в диапазоне 0-{N}: ", end = ' ')
k = int(input())

def mult_matrix_k(list_1, m, n, k):
    mul = []
    for i in range(0, m):
        temp = []
        for j in range(0, n):
            temp.append(list_1[i][j] * list_1[i][k])
        mul.append(temp)
    print(f"Матрица после перемножения на столбец {k}:")
    for i in range(0, m):
        for j in range(0, n):
            print(mul[i][j], end=' ')
        print()
    return mul

mul = mult_matrix_k(matrix, M, N, k)
'''

print('===================== Zadanie 11 =====================')
print('Суммирование элементов со строкой \'L\' в матрице MxN\nиз предыдущей задачи\n')
'''
11*. Реализовать функцию, которая суммирует элементы
каждой строки матрицы с соответствующими элементами L-й
строки (матрица M x N).
'''
'''
print(f"Введите номер L-й строки, с элементами которой будем складывать все строки,"
      f"\nон должен быть в диапазоне 0-{M-1}: ", end = ' ')
l = int(input())

def sum_matrix_l(list_1, m, n, l):
    new_matrix = []
    for i in range(0, m):
        temp = []
        sum = 0
        for j in range(0, n):
            sum = list_1[i][j] + list_1[l][j]
            temp.append(sum)
        # print(temp)
        new_matrix.append(temp)
    print(f"Матрица после сложения со строкой {l}:")
    for i in range(0, m):
        for j in range(0, n):
            print(new_matrix[i][j], end=' ')
        print()
    return new_matrix

sum_rows = sum_matrix_l(matrix, M, N, l)
'''

print('===================== Zadanie 12 =====================')
print('Определить в каких столбцах есть число \'H\' в матрице MxN\nиз предыдущей задачи\n')
'''
12. Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы
одно такое же число, а какие не имеют (матрица M x N)
'''
H = int(input("Введите искомое число 'H': "))

def where_H(list_1, m, n, h):
    where = []
    for i in range(0, n):
        counter = 0
        for j in range(0, m):
            if list_1[j][i] == h:
                counter += 1
        if counter > 0:
            where.append(i)
    return where

wh = where_H(matrix, M, N, H)
if len(wh) > 0:
    print(f"Число {H} содержится в следующих столбцах:")
    print(wh)
else:
    print(f"Число {H} в матрице отсутствует")