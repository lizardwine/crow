import os
import getpass
import colorama
from colorama import Fore, Style
from constants import *
from Db import Db

colorama.init(autoreset=True)

def newPass(uname, db):
	account = input("account: ")
	if account.count("@") == 1 and account.endswith(".com"):
		page = account.split("@")[-1]
	else:
		page = input("page: ")
		email = input("email: ")
			
		length = input("length(void for 32): ")
		length = 32 if not length.isdigit() else int(length)
		db.reg_pass(uname,account,page,email,length)

def readPass(db):
	variable_index = 6
	for var in ["uname", "email", "page", "account"]:
		if variable != "":
			break
		variable = input(f"{var}: ")
		variable_index -= 1
		variable_name = var

	password_found = False
	for i in db.read_pass():
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

if __name__ == "__main__":
	db = Db(filePsw)

	i = 0
	while i < 3:
		password = getpass.getpass("password(hided for security): ")
		if password == open(filePsw).read():
			opc = None
			#threading.Thread(target = timer).start()
			break
		elif i == 2 and password == "-1":
			i = 0
		elif password == "0":
			break
		i += 1

	os.system("cls")
	while opc != "0":
		opc = input(OPTIONS + " ").strip()
		if opc == "0":
			break
		os.system("cls")
		print(OPTIONS,opc)
		uname = input("unique name: ")
		if opc == "1":
			newPass(uname, db)
		elif opc == "2":
			readPass(db)	
		elif opc == "3":
			length = input("length(void for 32): ")
			length = 32 if not length.isdigit() else int(length)
			db.renew_pass(uname,length)	
		elif opc == "4":
			db.delete_pass(uname)
		elif opc == "5":
			new_pass = input("new_pass: ")
			db.change_pass(uname,new_pass)
		elif opc == "6":
			nuname = input("new unique name: ")
			db.change_uname(uname,nuname)
		elif opc == "7":
			email = input("email: ")
			db.change_email(uname,email)
		elif opc == "8":
			account = input("account: ")
			db.change_account(uname,account)
		elif opc == "9":
			page = input("page: ")
			db.change_page(uname,page)
		elif opc == "cls" or opc == "clear":
			os.system("cls")
		else:
			print(f'no there the option "{opc}"')
	os.system("cls")
