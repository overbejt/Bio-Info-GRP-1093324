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
    for line in file:
        if line[0] is not '#':
            line = line.strip()
            arr = line.split('\t')
            for a in range(len(arr)):
                print('{0}: {1}'.format(a, arr[a]))
    # with conn.cursor() as cursor:
    #     # Create a new record
    #     sql = "select * from overbejt.gene"
    #     cursor.execute(sql)
    #     data = cursor.fetchall()
    #     for i in data:
    #         print(i)

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

