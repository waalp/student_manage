import pymysql

def MySQL_connect():
    try:
        db = pymysql.connect("localhost","root","97320010231","user")
        # cursor = db.cursor()
        return db
    except:
        print('error connecting the database')
        return 0


def inser_info(name,age,score):
    db = MySQL_connect()
    cursor = db.cursor()
    # cursor.execute("drop table if EXISTS USER ")
    # data = cursor.fetchone()
    # print(nameget,ageget,scoreget)
    sql = "INSERT INTO student(name,age,score) VALUES (\'" + name + "\'," + age + "," + score + ")"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()

    except:
        db.rollback()
    db.close()