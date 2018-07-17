import xlrd

file_location = "./test2.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print sheet.cell_value(0,0)
# Name

print sheet.nrows
# 4

print sheet.ncols
# 3

for col in range(sheet.ncols):
	print sheet.cell_value(0, col)
# Name
# Age
# City

for col in range(sheet.ncols):
	print sheet.cell_value(2, col)
# Xyz
# 30.0
# Pune

data = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
print data
# [[u'Name', u'Vishal', u'Xyz', u'Abc'], [u'Age', 28.0, 30.0, 22.0], [u'City', u'Mumbai', u'Pune', u'Delhi']]

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print data
# [[u'Name', u'Age', u'City'], [u'Vishal', 28.0, u'Mumbai'], [u'Xyz', 30.0, u'Pune'], [u'Abc', 22.0, u'Delhi']]

print sheet.cell_type(1,2)
# 1
print sheet.cell_type(1,1)
# 2