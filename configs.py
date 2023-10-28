
from sqlalchemy import create_engine

def db_connection(database = 'dashboard'):
    
    user='root'
    password='240699'
    host='127.0.0.1:3306'
    database=database
    
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
    try:
        connection = engine.connect()
        return connection
    except Exception as e:
        raise e
    
    
