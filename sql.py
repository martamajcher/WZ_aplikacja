import os

db_file =  'C:\Users\mm\PycharmProjects\pythonProject\django\project_wz\db'
if os.path.exists(db_file):
    os.remove(db_file)
    print("Baza danych została usunięta.")
else:
    print("Baza danych nie istnieje.")