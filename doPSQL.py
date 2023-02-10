import psycopg2

def do_Sql(plyk):
    hostname = 'localhost'
    database = 'Raben'
    username = 'postgres'
    pwd = 'Wisnia12'
    port_id = 5432
    conn = None
    cur = None

    create_script_test = ''' CREATE TABLE IF NOT EXISTS pogoda (
                            id SERIAL PRIMARY KEY,
                            data VARCHAR(20),
                            opad REAL)'''

    copy_value = f"copy pogoda (data,opad) FROM 'C:/Nowy_folder/{plyk}.csv' DELIMITER ',' ENCODING 'UTF8';"

    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

        cur = conn.cursor()
        # cur.execute(create_script_test)

        cur.execute(copy_value)

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

