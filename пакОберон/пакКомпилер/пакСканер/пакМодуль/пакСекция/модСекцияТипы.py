# coding:utf8
"""
Жёстко прописанная секция IMPORT
"""
if True:
	from .модСекция import тСекция

class тСекцияТипы(тСекция):
	def __init__(сам, пДанные):
		тСекция.__init__(сам, пДанные)
		if пДанные['секция'] != "TYPE":
				assert False, "тСекцияТипы: ошибочное использование типа в секции TYPE, секция=" + пДанные['слова']
