import sqlalchemy
import sys

def get_wells(connection_string, depth, gradient):
    engine = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    
    query = """SELECT latitude, longitude, depth, gradient
               FROM wells
               WHERE depth > {} AND gradient > {};"""
    r = conn.execute(query.format(depth, gradient))
    
    return r.fetchall()

if __name__ == '__main__':
    depth = sys.argv[1]
    gradient = sys.argv[2]
    cs = sys.argv[3]

    print(sys.argv)

    print(get_wells(cs, depth, gradient))