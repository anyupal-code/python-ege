# 1. Сумма цифр числа
print("=== 1. Сумма цифр числа ===")
n = 12345
total = sum(int(el) for el in str(n))
print(f"Сумма цифр {n} = {total}") # 15

# 2. Сумма чётных чисел в списке
print("\n=== 2. Сумма чётных чисел ===")
numbers = [1, 2, 3, 4, 5, 6]
total_even = sum(x for x in numbers if x % 2 == 0)
print(f"Сумма чётных: {total_even}") # 12

# 3. Количество чётных чисел в списке
print("\n=== 3. Количество чётных чисел ===")
count_even = sum(1 for x in numbers if x % 2 == 0)
print(f"Количество чётных: {count_even}") # 3

# 4. Сумма цифр двоичного числа
print("\n=== 4. Сумма цифр двоичного числа ===")
nb = '10101111'
total_binary = sum(int(el) for el in nb)
print(f"Сумма цифр строки '{nb}': {total_binary}") # 6

# 4.1. Изящный вариант (количество единиц)
print("\n=== 4.1. Количество единиц ===")
nb2 = '101010111'
count_ones = nb2.count('1')
print(f"Количество единиц в '{nb2}': {count_ones}") # 6