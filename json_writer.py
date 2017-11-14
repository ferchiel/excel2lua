#!/usr/bin/env python
# coding=utf-8


class json_writer():
	"""write json file ..."""
	__file = None
	__name = None
	__table = 0
	__insert_line = False

	def __init__(self, output_file):
		aname = output_file
		_path = ''
		idx = aname.rfind('/')
		if idx != -1:
			_path = aname[:idx + 1]
			aname = aname[idx + 1:]
		idx = aname.find('.')
		if idx != -1:
			aname = aname[: idx]
		self.__name = aname
		self.__file = open(_path + aname + '.json', 'w', encoding = 'utf8')

	def __del__(self):
		self.__file.close()

	def _line(self):
		if self.__insert_line:
			self.__file.write(',\n')

	def write_beg(self):
		self.__table += 1
		s = '{\n'
		self.__file.write(s)
		self.__insert_line = False

	def write_end(self):
		self.__table -= 1
		s = '\n}'
		self.__file.write(s)

	def table_beg(self, name, _type):
		self._line()
		s = ''
		for x in range(self.__table):
			s += '\t'

		s += '"' + str(name) + '" : {\n'
		self.__file.write(s)
		self.__table += 1
		self.__insert_line = False

	def table_end(self):
		self._line()
		s = ''
		for x in range(self.__table - 1):
			s += '\t'
		s += '}'
		self.__file.write(s)
		self.__table -= 1
		self.__insert_line = True

	def attribute(self, key, value, _type):
		self._line()
		s = ''
		for x in range(self.__table):
			s += '\t'
		s += '"' + key + '" : '
		if _type == 'int':
			if int(value) == value:
				value = int(value)
			value = str(value)
			s += value
		elif _type == 'str':
			value = str(value)
			s += '\"' + value + '\"'
		elif _type == 'ints':
			s += '[ '
			tab = str(value).split(',')
			for v in tab:
				s += v + ', '
			s = s[: -2]
			s += ' ]'
		elif _type == 'strs':
			s += '[ '
			tab = value.split('`')
			for v in tab:
				s += '\"' + v + '\", '
			s = s[: -2]
			s += ' ]'
		elif _type == 'pos':
			tab = value.split(',')
			assert( len( tab ) == 2 )
			s += '{ "x" : ' + tab[0] + ', "y" : ' + tab[1] + ' }'
		elif _type == 'rect':
			tab = value.split(',')
			assert( len( tab ) == 4 )
			s += '{ "x" : ' + tab[0] + ', "y" : ' + tab[1] + ', "w" : ' + tab[2] + ', "h" : ' + tab[3] + ' }'
		else:
			print('MAKE ERROR! FILE: lua_writer.py  LINE: 62')
			exit(0)
		# s += ',\n'
		self.__file.write(s)
		self.__insert_line = True
