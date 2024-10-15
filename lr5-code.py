 Функция для проверки, все ли символы в строке являются строчными буквами
def is_all_lowercase(row):
    for char in row:
        if not char.islower():  # Если хотя бы один символ не строчная буква
            return False
    return True

# Функция для поиска строк с только строчными буквами в массиве
def find_lowercase_rows(matrix, matrix_name):
    lowercase_rows = []
    for i, row in enumerate(matrix):  # Проходим по строкам массива
        if is_all_lowercase(row):     # Проверяем, что все символы в строке строчные
            lowercase_rows.append(i + 1)  # Нумерация строк начинается с 1
    
    # Вывод результата для данного массива
    if lowercase_rows:
        print(f"В массиве {matrix_name} строки с номерами, содержащие только строчные буквы: {lowercase_rows}")
    else:
        print(f"В массиве {matrix_name} нет строк, содержащих только строчные буквы.")

# Тестовые массивы для отладки программы
def run_tests():
    # Тест 1: Оба массива содержат строки с только строчными буквами
    matrix1 = [
        ['а', 'б', 'в'],
        ['г', 'д', 'е'],
        ['ж', 'з', 'и']
    ]
    matrix2 = [
        ['А', 'б', 'В'],
        ['а', 'б', 'в'],
        ['д', 'е', 'ё']
    ]
    print("Тест 1:")
    find_lowercase_rows(matrix1, "Массив 1")
    find_lowercase_rows(matrix2, "Массив 2")
    print()

    # Тест 2: Один из массивов не содержит строк с только строчными буквами
    matrix3 = [
        ['А', 'Б', 'В'],
        ['Г', 'Д', 'Е'],
        ['Ж', 'З', 'И']
    ]
    matrix4 = [
        ['а', 'б', 'в'],
        ['а', 'б', 'В'],
        ['г', 'д', 'е']
    ]
    print("Тест 2:")
    find_lowercase_rows(matrix3, "Массив 3")
    find_lowercase_rows(matrix4, "Массив 4")
    print()

    # Тест 3: Оба массива не содержат строк с только строчными буквами
    matrix5 = [
        ['А', 'Б', 'В'],
        ['Г', 'Д', 'Е'],
        ['Ж', 'З', 'И']
    ]
    matrix6 = [
        ['А', 'Б', 'В'],
        ['А', 'Б', 'Г'],
        ['Д', 'Е', 'Ё']
    ]
    print("Тест 3:")
    find_lowercase_rows(matrix5, "Массив 5")
    find_lowercase_rows(matrix6, "Массив 6")
    print()

# Вызов тестов для отладки
run_tests()
