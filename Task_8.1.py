#  Напишите функцию, которая преобразует pickle файл хранящий список 
# словарей в табличный csv файл. Для тестированию возьмите pickle 
# версию файла из предыдущей задачи. Функция должна извлекать ключи 
# словаря для заголовков столбца из переданного файла.

import pickle
import csv

def convert(file_name):
    with (open(file_name, 'rb') as f_pic,
          open('new_permission.csv', 'w', newline='', encoding='utf-8',) as new_csv):
        picl_load = (pickle.load(f_pic))
        field = []
        rows = []
        for item in picl_load:
            rows.append(item)
            for key in item:
                if key not in field:
                    field.append(key)
        level, id_p, name, hash_name = field
        csv_write = csv.DictWriter(new_csv, fieldnames=[level, id_p, name, hash_name])
        csv_write.writeheader()
        csv_write.writerows(rows)

if __name__ == '__main__':
    convert('file_gb.pickle')
