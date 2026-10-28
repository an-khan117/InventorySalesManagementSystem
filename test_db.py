
from db import get_db_connection

try:
    connection = get_db_connection()
    print("Database connected successfully!")

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    result = cursor.fetchone()

    print("Total products:", result[0])

    cursor.close()
    connection.close()

except Exception as error:
    print("Database connection failed:", error)
