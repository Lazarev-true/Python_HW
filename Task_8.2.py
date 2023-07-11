# Прочитайте созданный в прошлом задании csv файл 
# без использования csv.DictReader. 
# Распечатайте его как pickle строку.

import csv
import pickle

def convert_csv(csv_file, file_name):
    with (open(file_name, 'bw') as f_pic,
          open(csv_file, "r", newline='', encoding='utf-8', ) as csv_f,
          ):
        list_csv = []
        read = csv.reader(csv_f)
        for item in read:
            list_csv.append(item)
        pickle.dump(list_csv, f_pic)
    with open(file_name, 'br') as f_pic:
        print(*f_pic)

if __name__ == '__main__':
    convert_csv("new_permission.csv", "file_csv.pickle")
    