"""
Here we are storing all the details such as locators, its type and the value in the excel
and storing it in the form of dictionary in this reading_reg python file. This is further
used in POM folder files while writing business logic

Ezample
txt_lname: ('id', 'LastName')

"""

import xlrd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "reg_data.xlsx")
# reg_path = r"C:\Users\Vishal Kirthic\PycharmProjects\framework_seleniumM7\data\reg_data.xlsx"

def read_reg():
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name("reg_details")
    rows = worksheet.get_rows()
    print(rows)
    header = next(rows)
    return {row[0].value: (row[1].value, row[2].value) for row in rows}

# print(read_reg())
reg_objects = read_reg()
print(reg_objects)
