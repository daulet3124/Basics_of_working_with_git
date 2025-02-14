import os
import datetime

# Функция для чтения содержимого файла
def read_file(file_path):
    """Чтение содержимого файла"""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

# Функция для записи текста в файл
def write_file(file_path, content):
    """Запись нового содержимого в файл"""
    with open(file_path, 'w') as file:
        file.write(content)

# Функция для обновления текста в файле
def update_text_in_file(file_path):
    """Обновление текста в файле с добавлением времени изменения"""
    text = read_file(file_path)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if text is not None:
        print(f"Текущий текст в файле:\n{text}")
        # Добавляем новую строку с меткой времени
        new_text = text + f"\nUpdated on {current_time} by Python program."
    else:
        print(f"Файл {file_path} не найден. Создаем новый файл.")
        # Если файл не найден, создаем новый с начальным текстом и датой создания
        new_text = f"This is a new file created by Python program.\nCreated on {current_time}."

    write_file(file_path, new_text)
    print(f"Обновленный текст:\n{new_text}")

if __name__ == "__main__":
    file_path = "example.txt"
    update_text_in_file(file_path)
