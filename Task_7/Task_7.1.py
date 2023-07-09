# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: 
# <original_name>_<new_name>_<position>.<new_extention>

import os

def renaming_files(files: list, new_name: str, extension: str, new_extension: str):
    count = 0
    for file in files:
        exten = file.split(".")
        if exten[-1] == extension:
            count += 1
            renamed_file = f'{new_name}_{str(count)}.{new_extension}'
            os.rename(f'{file}', f'{renamed_file}')
            print('=====================')
            print(f'{renamed_file = }')
        else:
            print('=====================')
            print(f'other_file = {file}')
if __name__ == '__main__':
    files_list = ['Kostik.txt', 'Last_file.md', 'Lazarev.txt', 'File.doc']
    renaming_files(files_list, 'GB_Lazarev', 'txt', 'md')
print('=====================')
