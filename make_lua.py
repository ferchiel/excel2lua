#!/usr/bin/env python
# coding=utf-8

import os
import config
import excel_reader
import lua_writer

import sys

conf = config.Config('excel_conf.conf')

def get_to_list(reader, key, _list):
	reader.sel_col(0)
	reader.sel_row(key)
	value = reader.get()
	_list.append(value)
	while True:
		value = reader.next_col()
		if not value:
			break
		_list.append(value)

def gen_line(reader, writer, line, key_tab, type_tab):
	key = reader.get_col_row(conf.key_col, line)
	if not key:
		return
	writer.table_beg(key, type_tab[conf.key_col])
	reader.sel_col(0)
	reader.sel_row(line)
	value = reader.get()
	if value != None:
		writer.attribute(key_tab[0], value, type_tab[0])
	for idx in range(1, reader.get_ncols()):
		key = key_tab[idx]
		value = reader.next_col()
		_type = type_tab[idx]
		if value != None:
			writer.attribute(key, value, _type)

	writer.table_end()


def gen_sheet(reader, writer):
	key_tab = list()
	type_tab = list()

	conf.key_row = int(conf.key_row)
	conf.type_row = int(conf.type_row)
	conf.key_col = int(conf.key_col)

	get_to_list(reader, conf.key_row, key_tab)
	get_to_list(reader, conf.type_row, type_tab)

	assert(key_tab[conf.key_col] and type_tab[conf.key_col] and len(key_tab) == len(type_tab))
	for line in range(int(conf.start_row), reader.get_nrows()):
		gen_line(reader, writer, line, key_tab, type_tab)

	del key_tab
	del type_tab


def make_style_1(reader, writer):
	reader.sel_sheet(0)
	gen_sheet(reader, writer)

def make_style_2(reader, writer):
	for idx in range(reader.len_sheet()):
		reader.sel_sheet(idx)
		writer.table_beg(reader.sheet_name(), 'str')
		gen_sheet(reader, writer)
		writer.table_end()

for filename in os.listdir(conf.inpath):
	if filename.startswith('~$'):
		continue
	check = False
	fullinpath = conf.inpath + filename
	fulloutpath = conf.outpath + filename
	if not os.path.isfile(conf.inpath + filename):
		continue
	for exname in conf.exnames:
		if filename.find(exname) != -1:
			check = True
			break

	if not check:
		continue

	reader = excel_reader.Excel_reader(fullinpath)
	writer = lua_writer.lua_writer(fulloutpath)

	print('translate:\n' + fullinpath + '\noutput file:\n' + fulloutpath + '\n\n')
	writer.write_beg()
	eval('make_style_' + conf.style)(reader, writer)
	writer.write_end()

	del reader
	del writer


print('excel2lua finished!')

