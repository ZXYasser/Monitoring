import sqlite3

# Connect to the database
conn = sqlite3.connect('lectures.db')
c = conn.cursor()

# Execute the SQL command to add the column
c.execute("ALTER TABLE lectures ADD COLUMN lecture_time TEXT;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
