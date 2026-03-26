
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bookstore",
    user="postgres",
    password="dhruvi",   # replace with your password
    host="localhost",
    port="5433"                 # change if your port is different
)

# Create cursor
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM books")

# Fetch data
data = cursor.fetchall()

# Print data
print(data)

# Close connection
cursor.close()
conn.close()