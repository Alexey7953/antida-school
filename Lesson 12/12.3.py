import sqlite3
with sqlite3.connect('example.db') as connection:

    cursor = connection.cursor()
    cursor.execute(
        """
            SELECT car.make
            FROM car
                JOIN carcolor ON car.id = carcolor.car_id
            GROUP BY car.id
            HAVING COUNT(carcolor.id) = 1;
        """
    )

    for entry in cursor.fetchall():
        print(entry)