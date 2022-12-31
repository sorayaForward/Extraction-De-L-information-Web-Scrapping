import sqlite3
from sqlite3 import Error
import json


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_posologie(conn, posologie):
    """
    Create a new posologie into the posologies table
    :param conn:
    :param posologie:
    :return: posologie id
    """
    sql = ''' INSERT INTO posologies(id,posologie)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, posologie)
    conn.commit()
    return cur.lastrowid


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    c.close()


def main():
    database = r".\\sqlite\\posologies.db"

    sql_create_posologies_table =  """CREATE TABLE IF NOT EXISTS posologies (
                                        id integer PRIMARY KEY,
                                        posologie text
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create posologies table
        create_table(conn, sql_create_posologies_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        # create a new posologie
        i = 1
        with open('posologie.json','r') as f:
            data = json.load(f)
            for po in data[0]['posologie']:
                posologie = (i, po);
                posologie_id = create_posologie(conn, posologie)
                i = i + 1

 



if __name__ == '__main__':
    main()