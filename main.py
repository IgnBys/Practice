import pandas as pd
import xlsxwriter as xlsxwriter

date, type, order, adress, needed_array = [], [], [], [], []
q = 0

with open("file.txt", "r" ,encoding='utf-8-sig') as file:
    char = file.read(1)
    for char in file:
        split_space = char.split(' ', 3)


        for element in split_space:
            if element != split_space[len(split_space) - 1]:
                element = element.replace(':', '').replace(',', '')
            if q == 0:
                right_date = element + '.2023'
                date.append(right_date)
            if q == 1:
                type.append(element)
            if q == 2:
                order.append(element)
            if q == 3:
                right_adress = element.replace('/n', '')
                adress.append(right_adress)
                q = -1
            q += 1

needed_array.append(date)
needed_array.append(type)
needed_array.append(order)
needed_array.append(adress)
workbook = xlsxwriter.Workbook('orders.xlsx')
worksheet = workbook.add_worksheet()
row = 0

for col, data in enumerate(needed_array):
    worksheet.write_column(row, col, data)
workbook.close()
file.close()
