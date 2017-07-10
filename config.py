#!/usr/bin/env python
# coding=utf-8

import os

class Config():
	"""config class"""
	# output style ...
	style = 1
	# input files, empty is ALL
	files = []
	# input files extern name
	exnames = None
	# key name`s line
	key_line = 1
	# type name`s line
	type_line = 2

	# input path
	inpath = os.getcwd()
	outpath = os.getcwd()

	# table key name count
	key_num = 1
	# table key row num
	key_row = []

	# start to compile line num
	start_line = 3

	def __init__(self, path):
		file = open(path)
		assert(file)
		for line in file:
			if len(line) <= 1 or line[0] == '#':
				continue

			idx = line.find('=')
			if idx != -1:
				key = line[:idx].strip()
				value = line[idx + 1:].strip()
				if value == '':
					continue
				if value.find(',') != -1:
					values = value.split(',')
					setattr(self, key, values)
					continue
				setattr(self, key, value)
		

# var = Config('excel_conf.conf')
# print(var.key_line, var.style)

