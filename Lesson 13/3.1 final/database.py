import sqlite3

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT phone, zip_code, city_id, street, home
        FROM seller JOIN account ON account.id=seller.account_id;
    """)
    for record in cursor.fetchall():
        print(record)
