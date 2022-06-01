import os
import getpass
flag = input("Are you sure?(Y/N): ").upper()
if flag == "Y":
    os.chdir(f"C:/Users/{getpass.getuser()}/crow")
    os.system("del /F/Q/S \".\" > NUL")
    os.chdir(f"C:/Users/{getpass.getuser()}")
    os.system("rmdir crow")
    os.system("del crow.exe")
