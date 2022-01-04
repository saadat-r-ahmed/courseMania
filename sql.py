def sql(query):
    
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "cse370_project"
    )


    cursor = db.cursor()
    cursor.execute(query)
    ret = cursor.fetchall()
    
    return ret


import mysql.connector

def insert_into_teacher(teacher_id, name, email, password, appointed_by):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cse370_project',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO teacher (teacher_id, name, email, password, appointed_by) 
                                VALUES (%s, %s, %s, %s, %s) """

        record = (teacher_id, name, email, password, appointed_by)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")