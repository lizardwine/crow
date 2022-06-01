import os
from rusia import moscu
from constants import *

# Functions
def Password():
    """ 
        asks for a password 
    """
    
    password = input("Type your password: ")
    rpassword = input("Repeat password: ")

    while password != rpassword:
        print("[ERROR] Password dom't match.")
        rpassword = input("repeat password: ")
    return password


def Creating(password):
    """
        create folderPsw and filePsw
    """

    print("[SUCCESS] Creating crow dirrectory. ")
    os.makedirs(folderPsw, exist_ok=True)

    print("[SUCCESS] Creating password file.")
    open(filePsw,"w").write(password)


def DataBase():
    """
        create dataBase filePsw
    """

    print("[SUCCESS] Creating database.")
    db = moscu(filePsw[:-4])
    db.execute(table)
    db.close()

# Main
if __name__ == "__main__":
    password = Password()
    Creating(password)
    
    print("[SUCCESS] Downloading executable.")
    with open("crow.exe", 'wb') as crowf:
        for chunk in crow.iter_content(chunk_size=1024):
            if chunk:
                crowf.write(chunk)
    DataBase()
    
    print("[FINISH] \n\n"
        "TYPE crow IN THE TERMINAL TO USE CROW\n")