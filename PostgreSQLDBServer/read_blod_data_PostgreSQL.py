# Read BLOB in the table 

import psycopg2 
from config import config 

def read_blob(part_id, path_to_dir):
    """ read BLOB data from a table """

    conn = None 

    try:
        # read databse configuration 
        params = config()

        # connect to the PostgreSQL databse 
        conn = psycopg2.connect(**params)

        # create a new cursor object 
        cur = conn.cursor()

        # execute the SELECT statement 

        cur.execute(""" SELECT part_name, file_extension, drawing_data
                        FROM part_drawings 
                        INNER JOIN parts on parts.part_id = part_drawings.part_id
                        WHERE parts.part_id= %s """, (part_id,))
        
        blob = cur.fetchone()
        print(blob)
        print(path_to_dir)
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])

        # close the communication with the PostgreSQL databse 
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == "__main__":
    read_blob(2, "D:\\Code\\git-repo\\PostgreSQLDBServer\\images\\blob\\")