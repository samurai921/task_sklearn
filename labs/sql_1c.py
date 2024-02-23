import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('organization.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS computers (
                    id INTEGER PRIMARY KEY,12365
                    purchase_date DATE,
                    price DECIMAL(10,2),
                    room_id INTEGER,
                    FOREIGN KEY (room_id) REFERENCES rooms(id))''')

# Вставка данных в таблицы (это можно сделать в другом месте программы, например, отдельными запросами)
cursor.execute("INSERT INTO rooms (name) VALUES (?)", ('Room 1',))
cursor.execute("INSERT INTO rooms (name) VALUES (?)", ('Room 2',))

cursor.execute("INSERT INTO computers (purchase_date, price, room_id) VALUES (?, ?, ?)", ('2024-02-23', 1500.00, 1))
cursor.execute("INSERT INTO computers (purchase_date, price, room_id) VALUES (?, ?, ?)", ('2024-02-23', 2000.00, 2))

conn.commit()

# Запрос данных с фильтрацией по заданному помещению
def get_computers_by_room(room_id):
    cursor.execute("SELECT * FROM computers WHERE room_id = ?", (room_id,))
    computers = cursor.fetchall()
    return computers

# Ввод пользователем id помещения
room_id = int(input("Введите id помещения: "))

# Получение списка компьютеров с фильтрацией по заданному помещению
computers = get_computers_by_room(room_id)

# Вывод информации о найденных компьютерах в текстовый файл
with open('computers_info.txt', 'w') as file:
    for computer in computers:
        file.write(f"ID: {computer[0]}, Дата покупки: {computer[1]}, Цена: {computer[2]}, ID помещения: {computer[3]}\n")

# Закрытие соединения с базой данных
conn.close()
