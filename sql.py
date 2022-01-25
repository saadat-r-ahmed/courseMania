import mysql.connector


def sql(query):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "cse370_project"
    )
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    ret = cursor.fetchall()
    return ret



def fetch_sql(query):
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



# ! FUNTIONS FOR IMPLEMENTING ADMINS FEATURES
def del_student_db(student_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='cse370_project',
                                            user='root')
        cursor = connection.cursor()

        # Delete a record
        sql_Delete_query = f"Delete from student where student_id = {student_id}"
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)


    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def del_teacher_db(teacher_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='cse370_project',
                                            user='root')
        cursor = connection.cursor()

        # Delete a record
        sql_Delete_query = f"DELETE FROM teacher where teacher_id = '{teacher_id}';"

        print(sql_Delete_query)
        cursor.execute(sql_Delete_query)
        connection.commit()
        print('number of rows deleted', cursor.rowcount)


    except mysql.connector.Error as error:
        print("Failed to delete record from table: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

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


# FUNCTIONS REQUIRED FOR IMPLEMENTING STUDENTS
def insert_into_enroll(student_id, course, semester):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cse370_project',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO enrolled_courses (student_id, course, semester)
                                VALUES (%s, %s, %s) """

        record = (student_id, course, semester)
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


def fetch_all_assesment(student_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "cse370_project"
    )

    query = f'''SELECT *
                FROM assesment
                WHERE (course, semester) IN
                    (select course, semester from enrolled_courses where student_id = {student_id})
                ORDER BY deadline desc;'''

    cursor = db.cursor()
    cursor.execute(query)

    ret = cursor.fetchall()
    return ret


def fetch_all_marks(student_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "cse370_project"
    )

    query = f'''SELECT course, semester, type, total_marks, achieved_marks
                FROM marks
                WHERE student_id = {student_id}
                ORDER BY course, semester, type;'''

    cursor = db.cursor()
    cursor.execute(query)

    ret = cursor.fetchall()
    return ret






# FUNCTIONS FOR TEACHER
def insert_into_assesment(course, semester, type, deadline, description, teacher_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cse370_project',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO assesment(course, semester, type, deadline, description)
                                VALUES(%s,%s,%s,%s,%s) """

        record = (course, semester, type, deadline, description)
        cursor.execute(mySql_insert_query, record)
        connection.commit()


        connection = mysql.connector.connect(host='localhost',
                                             database='cse370_project',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO ta_modifies(teacher_id, course, semester, type)
                                VALUES(%s,%s,%s,%s) """
        record = (teacher_id, course, semester, type)

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


def insert_into_marks(student_id, course, semester, type, total_marks, achieved_marks, updated_by):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cse370_project',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO marks(student_id, course, semester, type, total_marks, achieved_marks, updated_by)
                                VALUES(%s,%s,%s,%s,%s,%s,%s) """

        record = (student_id, course, semester, type, total_marks, achieved_marks, updated_by)
        cursor.execute(mySql_insert_query, record)
        connection.commit()

        print("Record inserted successfully into Marks table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
