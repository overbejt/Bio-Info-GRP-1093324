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
                # Check if it already exists
                sql = "select source_name from overbejt.source where source_name=%s"
                cursor.execute(sql, arr[1])
                res = cursor.fetchall()
                if len(res) < 1:
                    # Create a new record
                    sql = "insert into overbejt.source(source_name) values(%s)"
                    cursor.execute(sql, arr[1])
            conn.commit()
            # Insert the feature into the database eg: arr[2]
            with conn.cursor() as cursor:
                # Check if already exists
                sql = "select feature_id from overbejt.features where feature=%s"
                cursor.execute(sql, arr[2])
                res = cursor.fetchall()
                if len(res) < 1:
                    # Create a new feature entry
                    sql = "insert into overbejt.features(feature) values(%s)"
                    cursor.execute(sql, arr[2])
            conn.commit()
            # Insert the attributes into the database eg: arr[8]
            with conn.cursor() as cursor:
                # Check if already exists
                sql = "select attr_id from overbejt.attr where data=%s"
                cursor.execute(sql, arr[8])
                res = cursor.fetchall()
                if len(res) < 1:
                    # Create a new attributes entry
                    sql = "insert into overbejt.attr(data) values(%s)"
                    cursor.execute(sql, arr[8])
            conn.commit()

            # Fill in the gene table
            score = None if arr[5] is '.' else arr[5]
            frame = None if arr[7] is '.' else arr[7]
            with conn.cursor() as cursor:
                # Create a new gene entry
                sql = "replace into overbejt.gene(seqname, g_start, g_end, score, frame, a_id, f_id, s_id) "
                sql += "values(%s, %s, %s, %s, %s, "
                sql += "(select attr_id from overbejt.attr where data=%s ), "
                sql += "(select feature_id from overbejt.features where feature=%s), "
                sql += "(select source_id from overbejt.source where source_name=%s))"
                cursor.execute(sql, (arr[0], arr[3], arr[4], score, frame, arr[8], arr[2], arr[1]))
            conn.commit()
finally:
    conn.close()

