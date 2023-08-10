# Напишите код, который запускается из командной строки и получает 
# на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_file_info(path):
    for item in os.scandir(path):
        is_dir = item.is_dir()
        if is_dir:
            name = item.name
            extension = ''
        else:
            name, extension = os.path.splitext(item.name)
        parent_dir = os.path.basename(path)
        file_info = FileInfo(name, extension, is_dir, parent_dir)
        logging.info(str(file_info))

if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    get_file_info(path)
