import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (not to any database yet)
    connection = mysql.connector.connect(
        host="localhost",        
        user="root",    
        password="Lck9d$!9WzC$WTr2DXL7" 
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it doesn't already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"❌ Failed to connect or create database: {e}")

finally:
    # Close the cursor and connection properly
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
