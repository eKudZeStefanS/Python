import sqlite3

# Создание таблицы и заполнение её данными
conn = sqlite3.connect('first_table.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, col2 TEXT, col3 TEXT)')
cursor.execute('INSERT INTO my_table (col2, col3) VALUES (?, ?)', ('value1', 'value2'))
cursor.execute('INSERT INTO my_table (col2, col3) VALUES (?, ?)', ('value3', 'value4'))
cursor.execute('INSERT INTO my_table (col2, col3) VALUES (?, ?)', ('value5', 'value6'))

conn.commit()

cursor.execute('DELETE FROM my_table WHERE id = ?', (2,))
conn.commit()

cursor.execute('UPDATE my_table SET col2 = ?, col3 = ? WHERE id = ?', ('hello', 'world', 3))
conn.commit()

cursor.execute('SELECT id, col2, col3 FROM my_table')
with open('output.txt', 'w') as f:
    for row in cursor.fetchall():
        f.write(','.join(map(str, row)) + '\n')

conn.close()


conn = sqlite3.connect('second_table.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS my_text_table (text_col TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS my_number_table (number_col INTEGER)')

conn.commit()


my_list = ['Home', 'Work', 29, 9, 2022]

for value in my_list:
    if isinstance(value, str):
        cursor.execute('INSERT INTO my_text_table (text_col) VALUES (?)', (value,))
        cursor.execute('INSERT INTO my_number_table (number_col) VALUES (?)', (len(value),))
    elif value % 2 == 0:
        cursor.execute('INSERT INTO my_number_table (number_col) VALUES (?)', (value,))
    else:
        cursor.execute('INSERT INTO my_text_table (text_col) VALUES (?)', ('нечетное',))

    if cursor.execute('SELECT COUNT(*) FROM my_text_table').fetchone()[0] > 5:
        cursor.execute('DELETE FROM my_text_table WHERE rowid = 1')
    else:
        cursor.execute("UPDATE my_text_table SET text_col = 'hello' WHERE rowid = 1")

conn.commit()
conn.close()