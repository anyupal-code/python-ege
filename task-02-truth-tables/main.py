from itertools import product, permutations

print("=== 1. Основы: вложенные циклы ===")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                print(x, y, z, w)


print("\n=== 2. Основы: product ===")
for x, y, z, w in product([0, 1], repeat=4):
    print(x, y, z, w)


print("\n=== 3. Сложное выражение и приоритет ===")
# Выражение: ((x ≡ ¬y) → ¬(z → x)) ∨ ¬w
# Демонстрация того, как оно переводится в Python.
for x, y, z, w in product([0, 1], repeat=4):
    # Вариант 1: с использованием <= для импликации
    res1 = ((x == (not y)) <= (not (z <= x))) or (not w)
    # Вариант 2: с использованием not/or для импликации
    res2 = (not (x == (not y)) or (not (not z or x))) or (not w)
    
    # Убедимся, что оба варианта дают одинаковый результат
    if res1 != res2:
        print(f"Ошибка в переводе на наборе: {x}, {y}, {z}, {w}")
        
print("Все результаты совпали (выражение переведено верно).")
# Выведем первые 5 наборов для наглядности
print("Первые 5 наборов (x, y, z, w) -> Результат:")
count = 0
for x, y, z, w in product([0, 1], repeat=4):
    res = ((x == (not y)) <= (not (z <= x))) or (not w)
    print(f"{x}, {y}, {z}, {w} -> {int(res)}")
    count += 1
    if count == 5:
        break


print("\n=== 4. Более сложный вариант (Восстановление столбцов) ===")
# Функция F = x → ¬((y → z) ∧ (z ≡ ¬w))
# Записываем импликацию через <=, эквивалентность через ==
def f(x, y, z, w):
    return x <= (not ((y <= z) and (z == (not w))))

# Таблица из условия (прочерки заменены на a1..a5):
# 0  -  -  0 | 0
# -  1  1  - | 0
# -  1  0  0 | 0

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    st = [
        (0, a1, a2, 0),
        (a3, 1, 1, a4),
        (a5, 1, 0, 0)
    ]
    
    # В условии сказано, что строки различные
    if len(set(st)) == 3:
        # Перебираем все варианты сопоставления переменных столбцам
        for comb in permutations('xyzw'):
            # Проверяем, что при данном расположении букв f(x,y,z,w) везде равна 0
            if [f(**dict(zip(comb, r))) for r in st] == [0, 0, 0]:
                print(f"Найдено соответствие столбцов: {''.join(comb)}")

