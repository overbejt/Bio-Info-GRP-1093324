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
            # # Insert the source into the table eg: arr[1]
            # with conn.cursor() as cursor:
            #     # Create a new record
            #     sql = "insert ignore into overbejt.source(source_name) values(%s)"
            #     cursor.execute(sql, arr[1])
            # conn.commit()
            # # Insert the feature into the database eg: arr[2]
            # with conn.cursor() as cursor:
            #     # Create a new feature entry
            #     sql = "insert ignore into overbejt.features(feature) values(%s)"
            #     cursor.execute(sql, arr[2])
            # conn.commit()
            # # Insert the attributes into the database eg: arr[8]
            # with conn.cursor() as cursor:
            #     # Create a new attributes entry
            #     sql = "insert ignore into overbejt.attr(data) values(%s)"
            #     cursor.execute(sql, arr[8])
            # conn.commit()
            # Fill in the gene table
            with conn.cursor() as cursor:
                # Create a new gene entry
                sql = "insert ignore into overbejt.gene(seqname, g_start, g_end, score, frame, a_id, f_id, s_id) "
                sql += "values(%s, %s, %s, %s, %s, "
                sql += "(select attr_id from overbejt.attr where data=%s), "
                sql += "(select feature_id from overbejt.features where feature=%s), "
                sql += "(select source_id from overbejt.source where source_name=%s))"
                cursor.execute(sql, (arr[0], arr[3], arr[4], arr[5], arr[7], arr[8], arr[2], arr[1]))
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

