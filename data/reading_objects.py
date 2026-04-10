import xlrd
#print(xlrd)
path = r"C:\Users\Vishal Kirthic\PycharmProjects\framework_seleniumM7\data\locators.xlsx"

# xlrd.open_workbook(path)

def read_locator(page_name):
    workbook = xlrd.open_workbook(path)

    worksheet = workbook.sheet_by_name(page_name)
    rows = worksheet.get_rows()
    print(rows)
    header = next(rows)

    return {row[0].value: (row[1].value, row[2].value) for row in rows}


print(read_locator())


