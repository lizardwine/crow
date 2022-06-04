import threading
import time
import pickle
import os
import rusia
import random
import getpass
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
db = rusia.moscu(f"C:\\Users\\{getpass.getuser()}\\crow\\passwords")
def gen_number(Except = [34,39,92,96],fromto=[33,126]):
	r = random.randint(fromto[0],fromto[1])
	while r in Except:
		r = random.randint(fromto[0],fromto[1])
	return r

def gen_pass(length = 32,Ascii=[33,126]):
	password = ""
	for i in range(length):
		password += chr(gen_number())
	for i in range(10):
		if str(i) in password:
			break
	else:
		password += "124"
	return password
def reg_pass(uname,account,page,email,length = 32,Ascii=[33,126]):
	global opc
	password = gen_pass(length,Ascii)
	
	try:
		db.execute("INSERT INTO passwords VALUES(?,?,?,?,?,?)",(db.getid("passwords"),password,account,page,email,uname))
		print(f"{Style.DIM}{Fore.MAGENTA}{password}")
	except Exception as e:
		if str(e) == "UNIQUE constraint failed: passwords.uname":
			print("uique name already exist")
		else:
			print(e)
			opc = "0"
def read_pass():

	return list(db.execute("SELECT * FROM passwords"))
def renew_pass(uname,length = 32,Ascii=[33,126]):
	password = gen_pass(length,Ascii)
	print(f"{Style.DIM}{Fore.MAGENTA}{password}")
	db.execute("UPDATE passwords SET password = ? WHERE uname = ?",(password,uname,))
def delete_pass(uname):
	db.execute("DELETE FROM passwords WHERE uname = ?",(uname,))
def change_pass(uname,new_pass):
	db.execute("UPDATE passwords SET password = ? WHERE uname = ?",(new_pass,uname,))
def change_uname(uname,new_uname):
	db.execute("UPDATE passwords SET uname = ? WHERE uname = ?",(new_uname,uname,))
def change_page(uname,page):
	db.execute("UPDATE passwords SET page = ? WHERE uname = ?",(page,uname,))
def change_email(uname,email):
	db.execute("UPDATE passwords SET email = ? WHERE uname = ?",(email,uname,))
def change_account(uname,account):
	db.execute("UPDATE passwords SET account = ? WHERE uname = ?",(account,uname,))
opc = "0"
	
i = 0
while i < 3:
	password = getpass.getpass("password(hided for security): ")
	if str(hash(password)) == open(f"C:/Users/{getpass.getuser()}/crow/password.txt").read():
		opc = None
		#threading.Thread(target = timer).start()
		break
	elif i == 2 and password == "-1":
		i = 0
	elif password == "0":
		break
	i += 1
os.system("cls")
options = "0.-Exit\n1.-New pass\n2.-Read pass\n3.-Re-New pass\n===========\n4.-Delete pass\n5.-Change pass\n6.-Change unique name\n===========\n7.-Change email\n8.-Change account\n9.-Change page\n->"
while opc != "0":
	opc = input(options + " ").strip()
	os.system("cls")
	print(options,opc)
	if opc == "1":
		uname = input("unique name: ")
		account = input("account: ")
		if account.count("@") == 1 and account.endswith(".com"):
			page = account.split("@")[-1]
		else:
			page = input("page: ")
		email = input("email: ")
		
		length = input("length(void for 32): ")
		length = 32 if not length.isdigit() else int(length)
		reg_pass(uname,account,page,email,length)
	elif opc == "2":
		variable = input("uique name: ")
		variable_name = "uname"
		variable_index = 5
		if variable == "":
			variable = input("page: ")
			variable_index = 3
			variable_name = "page"
			if variable == "":
				variable = input("email: ")
				variable_index = 4
				variable_name = "email"
				if variable == "":
					variable = input("account: ")
					variable_index = 2
					variable_name = "account"

		password_found = False
		for i in read_pass():
			if variable == "*":
				print("======")
				print(f"{Fore.WHITE}unique name: ",end = ""); print(f"{Style.DIM}{Fore.RED}{i[5]}")
				print(f"{Fore.WHITE}account: ",end = ""); print(f"{Style.DIM}{Fore.YELLOW}{i[2]}")
				print(f"{Fore.WHITE}page: ",end = ""); print(f"{Style.DIM}{Fore.CYAN}{i[3]}")
				print(f"{Fore.WHITE}email: ",end = ""); print(f"{Style.DIM}{Fore.BLUE}{i[4]}")
				print(f"{Fore.WHITE}password: ",end = ""); print(f"{Style.DIM}{Fore.MAGENTA}{i[1]}")
				print()
			else:
				if i[variable_index] == variable:
					print("======")
					print(f"{Fore.WHITE}unique name: ",end = ""); print(f"{Style.DIM}{Fore.RED}{i[5]}")
					print(f"{Fore.WHITE}account: ",end = ""); print(f"{Style.DIM}{Fore.YELLOW}{i[2]}")
					print(f"{Fore.WHITE}page: ",end = ""); print(f"{Style.DIM}{Fore.CYAN}{i[3]}")
					print(f"{Fore.WHITE}email: ",end = ""); print(f"{Style.DIM}{Fore.BLUE}{i[4]}")
					print(f"{Fore.WHITE}password: ",end = ""); print(f"{Style.DIM}{Fore.MAGENTA}{i[1]}")
					print()
					password_found = True
		if not password_found:
			print(f"Password not found for {variable_name}: {variable}" if variable != "*" else "")
	elif opc == "3":
		uname = input("unique name: ")
		length = input("length(void for 32): ")
		length = 32 if not length.isdigit() else int(length)
		renew_pass(uname,length)	
	elif opc == "4":
		uname = input("unique name: ")
		delete_pass(uname)
	elif opc == "5":
		uname = input("unique name: ")
		new_pass = input("new_pass: ")
		change_pass(uname,new_pass)
	elif opc == "6":
		uname = input("unique name: ")
		nuname = input("new unique name: ")
		change_uname(uname,nuname)
	elif opc == "7":
		uname = input("unique name: ")
		email = input("email: ")
		change_email(uname,email)
	elif opc == "8":
		uname = input("unique name: ")
		account = input("account: ")
		change_account(uname,account)
	elif opc == "9":
		uname = input("unique name: ")
		page = input("page: ")
		change_page(uname,page)
	elif opc == "cls" or opc == "clear":
		os.system("cls")
	elif opc == "0":
		os.system("cls")
		break
	else:
		print(f'no there the option "{opc}"')
