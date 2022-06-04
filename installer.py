import requests as req
import os
import time
import getpass
import rusia
user = getpass.getuser()
password = input("type your password: ")
rpassword = input("repeat password: ")
while password != rpassword:
    print("password dom't match")
    rpassword = input("repeat password: ")
password = hash(password)
print("creating dir...")
os.system("mkdir \"C:/Users/%USERNAME%/crow\"")

open(f"C:/Users/{user}/crow/password.txt","w").write(str(password))
print("creating password file...")
url = 'https://github.com/lizardwine/crow/raw/main/crow.exe'
print("downloading executable")
crow = req.get(url, allow_redirects=True)

with open(f"C:/Users/{user}/crow.exe", 'wb') as crowf:
    for chunk in crow.iter_content(chunk_size=1024):
        if chunk:
            crowf.write(chunk)

print("creating database")
db = rusia.moscu(f"C:/Users/{user}/crow/passwords")

db.execute("""CREATE TABLE "passwords" (
    "id"    INTEGER UNIQUE,
    "password"  TEXT,
    "account"   TEXT,
    "page"  TEXT,
    "email" TEXT,
    "uname" TEXT UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT)
);""")

db.close()
print("finish...")
print("\nTYPE crow IN THE TERMINAL TO USE CROW\n")
os.system("pause")