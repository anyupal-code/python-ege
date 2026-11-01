from itertools import product

# 1. Основы: перебор слов
print("=== 1. Перебор слов ===")
for word in product(sorted('АБВ'), repeat=2):
    print(''.join(word))
print("\n")

# 2. Нумерация (через переменную n)
print("=== 2. Нумерация (через n) ===")
n = 0
for word in product('АБВ', repeat=3):
    n += 1
    s = ''.join(word)
    if s == 'БАВ':
        print(f'Слово БАВ стоит на позиции {n}')
        break

# 3. Нумерация (через enumerate)
print("\n=== 3. Нумерация (через enumerate) ===")
for index, word in enumerate(product('АБВ', repeat=3), start=1):
    s = ''.join(word)
    if s == 'БАВ':
        print(f'Слово БАВ стоит на позиции {index}')
        break

# 4. Подсчет количества
print("\n=== 4. Подсчет количества ===")
k = 0
for word in product('АБВ', repeat=3):
    s = ''.join(word)
    if s[0] == 'А':
        k += 1
print(f'Слов, начинающихся на А: {k}')

# 5. Работа с числами (как со строками)
print("\n=== 5. Числа как строки ===")
# Перебираем цифры как символы, проверяем на ведущий ноль
count = 0
for word in product('0123456789', repeat=3):
    s = ''.join(word)
    if s[0] != '0': # проверка на ведущий ноль
        count += 1
print(f'Трехзначных чисел (без ведущего нуля): {count}')

# 6. Работа с числами (как с числами)
print("\n=== 6. Числа как числа ===")
# Перебираем цифры как числа (range(10))
count_num = 0
for number in product(range(10), repeat=3):
    if number[0] != 0: # проверка на ведущий ноль
        count_num += 1
print(f'Трехзначных чисел (через числа): {count_num}')

# 7. Сложное условие (две буквы А, не стоящие рядом)
print("\n=== 7. Сложное условие ===")
count_a = 0
for word in product('АБВ', repeat=3):
    s = ''.join(word)
    # Ровно две А, и они не стоят рядом
    if s.count('А') == 2 and 'АА' not in s:
        count_a += 1
print(f'Слов с двумя А, стоящими не рядом: {count_a}')

