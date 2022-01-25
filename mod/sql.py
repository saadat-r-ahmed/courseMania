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