import sqlite3

class moscu:
	def __init__(self,name):
		self.con = sqlite3.connect(f'{name}.db')
		self.cur = self.con.cursor()

	def execute(self,code,add = (),commit = True):
		rs = ((code, add) if add != () else code)
		data = self.cur.execute(rs)
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
		
		return (int(ids[-1][idpos]) if ids != [] else 0) + 1

			