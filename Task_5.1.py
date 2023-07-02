# Напишите функцию, которая принимает на вход строку — абсолютный путь 
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, 
# расширение файла.

def parse_file_path(path):
    parts = path.split("/")
    file_name = parts[-1]
    extension = file_name.split(".")[-1]
    name = file_name.split(".")[0]
    path = "/".join(parts[:-1])
    return path, name, extension

path = '/User_Konstantin/Lazarev/Documents/diplom.doc'
parsed_path = parse_file_path(path)
print(parsed_path)
