from requests import get
from getpass import getuser

# installer
# --------------------------------------------------------------------
# Password folder Directory
user = getuser()
folderPsw = f"C:/Users/{user}/crow"

# Password file directory
filePsw = f"{folderPsw}/Password.txt"


url = 'https://github.com/lizardwine/crow/raw/main/crow.exe'
crow = get(url, allow_redirects=True)

# DataBase table
table = """CREATE TABLE "passwords" (
        "id"    INTEGER UNIQUE,
        "password"  TEXT,
        "account"   TEXT,
        "page"  TEXT,
        "email" TEXT,
        "uname" TEXT UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    );"""
# --------------------------------------------------------------------
# pass-manager
# --------------------------------------------------------------------

ERROR_REG_PASS = "UNIQUE constraint failed: passwords.uname"

UNIQUE_NAME = "unique name already exist"

CODE_REG_PASS = "INSERT INTO passwords VALUES(?,?,?,?,?,?)"
CODE_READ_PASS = "SELECT * FROM passwords"
CODE_RENEW_PASS = "UPDATE passwords SET password = ? WHERE uname = ?"
CODE_DELETE_PASS = "DELETE FROM passwords WHERE uname = ?"
CODE_CHANGE_PASS = "UPDATE passwords SET password = ?, uname = ? WHERE uname = ?"
CODE_CHANGE_UNAME = "UPDATE passwords SET uname = ? WHERE uname = ?"
CODE_CHANGE_PAGE = "UPDATE passwords SET page = ? WHERE uname = ?"
CODE_CHANGE_EMAIL = "UPDATE passwords SET email = ? WHERE uname = ?"
CODE_CHANGE_ACCOUNT = "UPDATE passwords SET account = ? WHERE uname = ?"

OPTIONS = "".join(["\n0.-Exit", "\n1.-New pass", "\n2.-Read pass", "\n3.-Re-New pass",
		  "\n===========",
		  "\n4.-Delete pass ", "\n5.-Change pass", "\n6.-Change unique name",
		  "\n===========",
		  "\n7.-Change email", "\n8.-Change account", "\n9.-Change page",
		  "\n->"])
