import xlrd


file_location = "./datas.xlsx"
workbook = xlrd.open_workbook(file_location)
users = workbook.sheet_by_index(0)
languages = workbook.sheet_by_index(1)

data_users = [[users.cell_value(r, c) for c in range(users.ncols)] for r in range(1, users.nrows)]
data_languages = [[languages.cell_value(r, c) for c in range(languages.ncols)] for r in range(1, languages.nrows)]


# zrobić plik excelowski z użytkownikami i językami
# metody do pozyskania emaila i hasła
