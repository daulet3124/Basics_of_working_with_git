# Пример программы, которая меняет содержимое файла

def read_file(file_path):
    """Чтение содержимого файла"""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def write_file(file_path, content):
    """Запись нового содержимого в файл"""
    with open(file_path, 'w') as file:
        file.write(content)

def update_text_in_file(file_path):
    """Обновление текста в файле"""
    text = read_file(file_path)
    if text is not None:
        print(f"Текущий текст в файле:\n{text}")
        # Изменим текст на новый
        new_text = text + "\nА ЭТА ЛИНИЯ БЫЛА ДОБАВЛЕНА ПРОГРАММОЙ."
        write_file(file_path, new_text)
        print(f"Обновленный текст:\n{new_text}")
    else:
        print(f"Файл {file_path} не найден.")

if __name__ == "__main__":
    file_path = "example.txt"
    update_text_in_file(file_path)
