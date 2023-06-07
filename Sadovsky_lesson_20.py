import sqlite3

conn = sqlite3.connect('my_database.db')

conn.execute('''CREATE TABLE tasks
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             DESCRIPTION    TEXT    NOT NULL,
             STATUS         TEXT    NOT NULL);''')

# добавляем задачи в таблицу

conn.execute("INSERT INTO tasks (ID, NAME, DESCRIPTION, STATUS) \
              VALUES (1, 'Посмотреть фильм', 'Посмотреть новый фильм в кинотеатре', 'в процессе')")

conn.execute("INSERT INTO tasks (ID, NAME, DESCRIPTION, STATUS) \
              VALUES (2, 'Сходить в магазин', 'Купить продукты на неделю', 'в ожидании')")

cursor = conn.execute("SELECT ID, NAME, DESCRIPTION, STATUS from tasks")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("DESCRIPTION = ", row[2])
   print("STATUS = ", row[3], "\n")

conn.close()
