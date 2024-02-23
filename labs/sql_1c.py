import sqlite3
import csv

# Создание подключения к базе данных
def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

# Создание таблиц
def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY,
                        name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS computers (
                        id INTEGER PRIMARY KEY,
                        purchase_date DATE,
                        price DECIMAL(10,2),
                        room_id INTEGER,
                        FOREIGN KEY (room_id) REFERENCES rooms(id))''')

# Вставка данных в таблицы
def insert_data(cursor):
    cursor.execute("INSERT INTO rooms (name) VALUES (?)", ('Room 1',))
    cursor.execute("INSERT INTO rooms (name) VALUES (?)", ('Room 2',))

    cursor.execute("INSERT INTO computers (purchase_date, price, room_id) VALUES (?, ?, ?)", ('2024-02-23', 1500.00, 1))
    cursor.execute("INSERT INTO computers (purchase_date, price, room_id) VALUES (?, ?, ?)", ('2024-02-23', 2000.00, 2))

# Запрос данных с фильтрацией по заданному помещению
def get_computers_by_room(cursor, room_id):
    cursor.execute("SELECT * FROM computers WHERE room_id = ?", (room_id,))
    computers = cursor.fetchall()
    return computers

# Запись данных в CSV
def write_data_to_csv(file_name, data):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for computer in data:
            writer.writerow(computer)



# Основная функция
def main():
    conn, cursor = connect_to_database('organization.db')
    create_tables(cursor)
    insert_data(cursor)
    conn.commit()

    room_id = int(input("Введите id помещения: "))
    computers = get_computers_by_room(cursor, room_id)
    
    # Вывод данных на экран (для отладки)
    print("Найденные компьютеры:")
    for computer in computers:
        print(computer)
    
    write_data_to_csv('computers_info.csv', computers)

    conn.close()

if __name__ == "__main__":
    main()
