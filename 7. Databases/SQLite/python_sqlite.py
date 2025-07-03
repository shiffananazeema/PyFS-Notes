import sqlite3

# Connect to a SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );''')

###########

# Insert data into the table


# cursor.execute('''INSERT INTO users (username, email) VALUES (?, ?)''', ('Shiffana', 'shiffana@gmail.com'))

# connection.commit()

#########

# Insert multiple rows at once

# users = [
#     ('Alice', 'alice@example.com'),
#     ('Bob', 'bob@example.com'),
#     ('Charlie', 'charlie@example.com')
# ]
# cursor.executemany('''INSERT INTO users (username, email) VALUES (?, ?)''', users)

#######

# Query the database
# cursor.execute('''SELECT * FROM users''')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

######

# Update a record
# cursor.execute('''UPDATE users SET email = ? WHERE username = ?''', ('alice@example.com', 'Alice'))

# Delete a record
# cursor.execute('''DELETE FROM users WHERE username = ?''', ('Bob',))

# Drop a table
# cursor.execute('''DROP TABLE IF EXISTS users''')

######

# Commit the changes and close the connection
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()