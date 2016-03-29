import xlrd

# Variables:
file_location = "./datas.xlsx"
workbook = xlrd.open_workbook(file_location)

# Users' sheet
users = workbook.sheet_by_index(0)
u_columns = users.ncols
u_rows = users.nrows
data_users = [[users.cell_value(r, c) for c in range(u_columns)] for r in range(1, u_rows)]

# Languages' sheet
languages = workbook.sheet_by_index(1)
l_columns = languages.ncols
l_rows = languages.nrows
data_languages = [languages.cell_value(r, 0) for r in range(1, l_rows)]


def get_email(name):
    for i in data_users:
        if name == i[1]:
            return i[2]


def get_password(name):
    for i in data_users:
        if name == i[1]:
            return i[4]
