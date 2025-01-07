import sqlite3 as sq, logging, datetime


def connnetctionToDatabase():

    try:

        connec=sq.Connection("userData.db")

        logging.info(f"[{datetime.datetime.now()}] :: Connection to database was successful")

        return connec

    except Exception as ex:

        logging.error(f"[{datetime.datetime.now()}] :: Connection to database was not successful, REASON: {ex}")


connection=connnetctionToDatabase()


def reqExecute(request: str):

    try:

        cursor=connection.cursor()

        cursor.execute(request)

        connection.commit()

        logging.info(f"[{datetime.datetime.now()}] :: Request execute was successful")

        return cursor.fetchall

    except Exception as ex:
        
        logging.error(f"[{datetime.datetime.now()}] :: Request execute was not successful, REASON: {ex}")

