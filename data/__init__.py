from sqlite3 import connect, IntegrityError
import os

db_name = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
conn = connect(db_name)
curs = conn.cursor()