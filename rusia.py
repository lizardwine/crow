import os,sqlite3

class moscu:
	def __init__(self,name):
		self.con = sqlite3.connect(f'{name}.db')
		self.cur = self.con.cursor()
	def execute(self,code,add = (),commit = True):
		data = ""
		if add != ():
			data = self.cur.execute(code,add)
		elif add == ():
			data = self.cur.execute(code)
		if commit:
			self.commit()
		return list(data)
	def commit(self):
		self.con.commit()
	def close(self):
		self.con.close()
	def getid(self,table,idpos = 0):
		ids = []
		for i in self.execute("SELECT * FROM {} ORDER BY id".format(table)):
			ids.append(i)
		if len(ids) >= 1:
			return int(ids[-1][idpos]) + 1
		return 1

			