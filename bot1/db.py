import sqlite3
import pandas as pd


def createTable():
    conn = sqlite3.connect('bookings.db')
    cur = conn.cursor()
    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS bookings(
        name TEXT PRIMARY KEY,
        user_id INTEGER,
        date INTEGER,
        time INTEGER,
        quantity INTEGER,
        payment_status TEXT
    ) 
    ''')
    conn.commit()
    conn.close()


def add_booking(user_id, date, time, quantity, payment_status):
    conn = sqlite3.connect('bookings.db')
    cur = conn.cursor()
    cur.execute(''' 
    INSERT INTO bookings (user_id, date, time, quantity, payment_status) 
    VALUES (?, ?, ?, ?, ?) 
    ''', (user_id, date, time, quantity, payment_status))
    print('Бронирование добавлено')
    conn.commit()
    conn.close()


def get_bookings_by_user(user_id):
    conn = sqlite3.connect('bookings.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM bookings WHERE user_id = ?', (user_id,))
    rows = cur.fetchall()
    conn.close()

    # Если хотите, можно преобразовать результат в DataFrame для удобства
    df = pd.DataFrame(rows, columns=['id', 'user_id', 'date', 'time', 'quantity', 'payment_status'])
    return df
