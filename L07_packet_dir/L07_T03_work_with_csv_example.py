import csv
# https://alexanderdyakonov.files.wordpress.com/2015/04/ama2015_pandas.pdf
# https://proglib.io/p/pandas-tricks/

'''
функция csv.reader
функция csv.writer
класс csv.Dictwriter
класс csv.DictReader
'''


# csv.writer
car_data = [['brand', 'price', 'year'],['Volvo', 1.5, 2017],['Lada', 0.5, 2018],['Audi', 2.0, 2018]]

with open('L07_T03_body_file_example.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&') #
    writer.writerows(car_data)
print('Writing complete!')

# csv.reader

with open('L07_T03_body_file_example.csv') as f:
    reader = csv.reader(f,delimiter = '&')
    for row in reader:
        print(row)

# csv.Dictwriter
data_dict = [{'Name': 'Dima', 'age': 28},
             { 'age': 29, 'Name': 'Kate'},
             {'Name': 'Mike', 'age': 31}]

fieldnames = ['Name','age']

with open('L07_T03_open_w_csv_example_1.csv', 'w') as f:
    writer = csv.DictWriter(f,delimiter = '&',fieldnames =  fieldnames)
    writer.writeheader()
    for i in range(len(data_dict)):
        writer.writerow(data_dict[i])

# csv.Dictreder

with open('L07_T03_open_w_csv_example_1.csv') as f:
    reader = csv.DictReader(f, delimiter = '&')
    for row in reader:
        print(dict(row))


import pandas as pd

DataFrame_from_csv = pd.read_csv('L07_T03_open_w_csv_example_1.csv', sep ='&')
print(type(DataFrame_from_csv))
print(DataFrame_from_csv)