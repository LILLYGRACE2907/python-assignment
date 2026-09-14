connection = None

try:
    print("Connecting to database...")
    connection = "Database Connection"
    print("Database connected")

except Exception:
    print("Connection error")

finally:
    if connection:
        print("Database connection closed")