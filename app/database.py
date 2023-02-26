import sqlalchemy
import sys
import os

def get_wells(depth, gradient):
    connection_string = os.getenv("DB_URL")
    engine = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    
    query = """SELECT latitude, longitude, depth, gradient
               FROM wells
               WHERE depth > %s AND gradient > %s;"""
    r = conn.execute(query, (depth, gradient))
    
    return r.fetchall()

if __name__ == '__main__':
    depth = sys.argv[1]
    gradient = sys.argv[2]

    print(sys.argv)

    print(get_wells(depth, gradient))