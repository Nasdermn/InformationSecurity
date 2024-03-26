from PIL import Image

# Открываем изображение
image = Image.open("1011.png")

# Получаем размеры изображения
width, height = image.size

# Создаем пустой массив для хранения последних двух бит каждого канала цвета
color_array = []

# Проходим по каждому пикселю изображения
for y in range(height):
    for x in range(width):
        # Получаем цвет пикселя в формате (R, G, B)
        pixel = image.getpixel((x, y))
        
        # Получаем последние два бита каждого канала цвета
        r_last_two_bits = bin(pixel[0])[-2:].zfill(2)
        g_last_two_bits = bin(pixel[1])[-2:].zfill(2)
        b_last_two_bits = bin(pixel[2])[-2:].zfill(2)
        
        # Добавляем в массив последние два бита каждого канала цвета
        color_array.append(r_last_two_bits)
        color_array.append(g_last_two_bits)
        color_array.append(b_last_two_bits)

# Выводим полученный массив
print('Массив 1')
print(color_array)

# Создаем пустой массив для хранения результатов
new_array = []

# Проходим по каждым 4 элементам исходного массива
for i in range(0, len(color_array), 4):
    # Если осталось менее 4 элементов, выходим из цикла
    if i + 3 >= len(color_array):
        break
    
    # Объединяем четыре элемента в строку
    combined_str = "".join(color_array[i:i+4])
    
    # Добавляем строку в новый массив
    new_array.append(combined_str)

# Убеждаемся, что символ 'b' удален из всех строк в новом массиве
new_array = [binary_str.replace('b', '') for binary_str in new_array]

# Выводим полученный массив
print('Массив 2')
print(new_array)

# Создаем пустой массив для хранения результатов
decimal_array = []

# Проходим по каждой строке в новом массиве
for binary_str in new_array:
    # Переводим строку из двоичной системы счисления в десятичную
    decimal_num = int(binary_str, 2)
    
    # Добавляем десятичное число в новый массив
    decimal_array.append(decimal_num)

# Выводим полученный массив
print('Массив 3')
print(decimal_array)

# Создаем пустую строку для хранения результата
decoded_string = ""

# Проходим по каждому числу в массиве decimal_array
for decimal_num in decimal_array:
    # Проверяем, что число находится в диапазоне от 0 до 255
    if 0 <= decimal_num <= 255:
        # Получаем символ из кодировки по его ASCII коду
        char = chr(decimal_num)
        # Добавляем символ к результату
        decoded_string += char
    else:
        # Если число не входит в диапазон от 0 до 255, добавляем символ "?" к результату
        decoded_string += "?"

# Выводим результат в виде строки
print("Декодированная строка:")
print(decoded_string)