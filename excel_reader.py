#!/usr/bin/env python
# coding=utf-8


import sys, xlrd

class Excel_reader:
	"""excel reader apis"""
	__sheets = None
	__cur_sheet = None
	__cur_row = None
	__cur_col = None

	def __init__(self, path):
		data = xlrd.open_workbook(path)
		self.__sheets = list()
		for x in range(data.nsheets):
			obj = data.sheet_by_index(x)
			self.__sheets.append(obj)

	def __del__(self):
		del self.__sheets

	def len_sheet(self):
		return len(self.__sheets)

	def sel_sheet(self, idx):
		if idx >= len(self.__sheets):
			return

		self.__cur_sheet = idx
		return self.__sheets[idx]

	def next_sheet(self):
		if self.__cur_sheet == None:
			return
		if self.__cur_sheet + 1 >= len(self.__sheets):
			return

		self.__cur_sheet += 1
		return self.__sheets[self.__cur_sheet]

	def sheet_name(self):
		if self.__cur_sheet == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		return sheet.name

	def sel_row(self, idx):
		if self.__cur_sheet == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		if idx >= sheet.nrows:
			return
		self.__cur_row = idx

	def sel_col(self, idx):
		if self.__cur_sheet == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		if idx >= sheet.ncols:
			return
		self.__cur_col = idx

	def get(self):
		if self.__cur_sheet == None or self.__cur_row == None or self.__cur_col == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		_value = sheet.cell_value(self.__cur_row, self.__cur_col)
		_type = sheet.cell_type(self.__cur_row, self.__cur_col)
		if _type == xlrd.XL_CELL_EMPTY or _value == '':
			return
		if (_type == xlrd.XL_CELL_NUMBER or _type == xlrd.XL_CELL_DATE) and int(_value) == _value:
			_value = int(_value)
		return _value

	def next_row(self):
		if self.__cur_sheet == None or self.__cur_row == None or self.__cur_col == None:
			return
		self.__cur_row += 1
		sheet = self.__sheets[self.__cur_sheet]
		if self.__cur_row >= sheet.nrows:
			return

		_value = sheet.cell_value(self.__cur_row, self.__cur_col)
		_type = sheet.cell_type(self.__cur_row, self.__cur_col)
		if _type == xlrd.XL_CELL_EMPTY or _value == '':
			return
		if (_type == xlrd.XL_CELL_NUMBER or _type == xlrd.XL_CELL_DATE) and int(_value) == _value:
			_value = int(_value)
		return _value

	def next_col(self):
		if self.__cur_sheet == None or self.__cur_row == None or self.__cur_col == None:
			return
		self.__cur_col += 1
		sheet = self.__sheets[self.__cur_sheet]
		if self.__cur_col >= sheet.ncols:
			return

		_value = sheet.cell_value(self.__cur_row, self.__cur_col)
		_type = sheet.cell_type(self.__cur_row, self.__cur_col)
		if _type == xlrd.XL_CELL_EMPTY or _value == '':
			return
		if (_type == xlrd.XL_CELL_NUMBER or _type == xlrd.XL_CELL_DATE) and int(_value) == _value:
			_value = int(_value)
		return _value

	def get_col_row(self, col, row):
		if self.__cur_sheet == None:
			return

		sheet = self.__sheets[self.__cur_sheet]
		if col >= sheet.ncols or row >= sheet.nrows:
			return

		_value = sheet.cell_value(row, col)
		_type = sheet.cell_type(row, col)
		if _type == xlrd.XL_CELL_EMPTY or _value == '':
			return
		if (_type == xlrd.XL_CELL_NUMBER or _type == xlrd.XL_CELL_DATE) and int(_value) == _value:
			_value = int(_value)
		return _value

	def get_ncols(self):
		if self.__cur_sheet == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		return sheet.ncols

	def get_nrows(self):
		if self.__cur_sheet == None:
			return
		sheet = self.__sheets[self.__cur_sheet]
		return sheet.nrows

# var1 = Excel_reader("test.xlsx")
# var1.sel_sheet(0)
# var1.sel_col(0)
# var1.sel_row(5)
# print(var1.get())


# var.sel_sheet(0)
# print(var.sheet_name())
# var.sel_col(1)
# var.sel_row(0)
# print(var.get())
# print(var.next_row())
# print(var.next_col())






