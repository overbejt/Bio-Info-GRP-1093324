import pymysql.cursors
import pymysql
import sys

print('hell0')

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       cursorclass=pymysql.cursors.DictCursor)
try:

    # open the file
    file = open(sys.argv[1], 'r')
    # Iterate through the contents
    for line in file:
        # Skip comments
        if line[0] is not '#':
            # Clean up the line and split it into an array
            line = line.strip()
            arr = line.split('\t')
            # Insert the source into the table eg: arr[1]
            with conn.cursor() as cursor:
                # Create a new record
                sql = "insert ignore into overbejt.source(source_name) values(%s)"
                cursor.execute(sql, arr[1])
            conn.commit()
            break

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # conn.commit()

    # with conn.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    conn.close()

