from rusia import moscu
from constants import *
from typing import Tuple
from random import randint
from colorama import Fore, Style

class Db(moscu):
	def __init__(self, file):
		super().__init__(file[:-4])

	def gen_number(self, Except = [34,39,92,96], fromto : Tuple[int,int] = (33,126)):
		a = fromto[0]
		b = fromto[1]
		r = randint(a,b)
		while r in Except:
			r = randint(a,b)
		return r

	def gen_pass(self,length = 32,Ascii=[33,126]):
		password = "".join([chr(self.gen_number()) for _ in range(length)])

		for i in range(10):
			if str(i) in password:
				break
			password += "124"
		return password

	def reg_pass(self,uname, account, page, email, length = 32, Ascii=[33,126]):
		password = self.gen_pass(length,Ascii)
		try:
			add = (self.getid("passwords"),password,account,page,email,uname)
			self.execute(CODE_REG_PASS , add)
			print(f"{Style.DIM}{Fore.MAGENTA}{password}")
		except Exception as e:
			if str(e) == ERROR_REG_PASS:
				print(UNIQUE_NAME)
			else:
				print(e)

	def read_pass(self):
		return list(self.execute(CODE_READ_PASS))

	def renew_pass(self,uname,length = 32,Ascii=[33,126]):
		password = self.gen_pass(length,Ascii)
		print(f"{Style.DIM}{Fore.MAGENTA}{password}")
	
		self.execute(CODE_RENEW_PASS,(password,uname,))

	def delete_pass(self,uname):
		self.execute(CODE_DELETE_PASS,(uname,))

	def change_pass(self,uname,new_pass):
		changePs = (new_pass,"".join(list(uname)[:-1]) + list(new_pass)[0],uname,)
		self.execute(CODE_CHANGE_PASS, changePs)

	def change_uname(self,uname,new_uname):
		self.execute(CODE_CHANGE_UNAME,(new_uname,uname,))

	def change_page(self,uname,page):
		self.execute(CODE_CHANGE_PAGE,(page,uname,))

	def change_email(self,uname,email):
		self.execute(CODE_CHANGE_EMAIL,(email,uname,))

	def change_account(self,uname,account):
		self.execute(CODE_CHANGE_ACCOUNT,(account,uname,))
