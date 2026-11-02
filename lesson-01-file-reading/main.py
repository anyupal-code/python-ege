print("=== 1. Одно число в строке ===")
s = list(map(int, open('one.txt')))
print(s) 

print("\n=== 2. Несколько чисел в строке ===")
for st in open('many.txt'):
    row = list(map(int, st.split()))
    print(row)

print("\n=== 2.1. Сразу в переменные ===")
for st in open('many.txt'):
    a, b, c = map(int, st.split())
    print(a, b, c)

print("\n=== 2.2 Наибольшее и произведение двух остальных в каждой строке===")
for st in open('many.txt'):
    row = list(map(int, st.split()))
    a, b, c = sorted(row)
    print(c, a * b)

print("\n=== 3. Непрерывная строка ===")
line = open('continuous.txt').readline()
print(line)