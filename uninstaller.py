import os
import getpass
flag = input("Are you sure?(Y/N): ").upper()
if flag == "Y":
    try:
        os.chdir(f"C:/Users/{getpass.getuser()}/crow")
        os.system("del /F/Q/S \".\" > NUL")
        os.chdir(f"C:/Users/{getpass.getuser()}")
        os.system("rmdir crow")
        os.system("del crow.exe")
        print("uninstalled succefully")
    except Exception as e:
        print("an error has ocurred")
        print("create an issue on https://github.com/lizardwine/crow/issues/new with:")
        print(str(e))

