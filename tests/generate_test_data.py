import csv
import random

# Списки для генерации случайных данных
positions = ["Ноутбук", "Смартфон", "Планшет", "Монитор", "Клавиатура", "Мышь", "Принтер", "Сканер", "Наушники", "Колонки"]

# Чтение марок из файла marks.csv
with open('data/marks.csv', 'r', encoding='utf-8') as marks_file:
    marks = [line.strip() for line in marks_file if line.strip()]

# Открываем файл для записи
with open('test_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Записываем заголовки
    writer.writerow(["Number of check", "name of position", "quantity", "price", "mark"])
    
    # Генерируем данные
    total_rows = 0
    check_number = 1

    while total_rows < 100:
        # Генерируем от 1 до 5 позиций для каждого чека
        positions_in_check = random.randint(1, 5)
        
        for _ in range(positions_in_check):
            position = random.choice(positions)
            quantity = random.randint(1, 10)
            price = round(random.uniform(100, 10000), 2)
            
            # 20% шанс, что поле mark будет пустым
            if random.random() < 0.2:
                mark = ""
            else:
                mark = random.choice(marks)
            
            writer.writerow([check_number, position, quantity, price, mark])
            total_rows += 1
            
            if total_rows >= 100:
                break
        
        check_number += 1

print(f"Файл 'test_data.csv' успешно создан. Всего строк: {total_rows}")
