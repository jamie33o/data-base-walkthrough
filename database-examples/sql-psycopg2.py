import psycopg2


#connect to "chinook" database
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "artist" table
#cursor.execute('SELECT * FROM "Artist"' )
#fetch the results (multiple)

# query 2 - select all records from the "artist" table
#cursor.execute('SELECT "Name" FROM "Artist"' )

# query 3 - select all records from the "artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"] )

# query 4 - select all records from the "artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', [51] )


results = cursor.fetchall()

#fetch the results single
# results = cursor.fetchone()

#close the connection
connection.close()

# print results 
for result in results:
    print(results)