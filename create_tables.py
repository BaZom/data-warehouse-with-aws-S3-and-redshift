import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list from sql_queries.py.
    Args:
        curr (obj): object of curser class
        conn (obj): connection object 
        
    Returns:
        no return values
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list from sql_queries.py.
    Args:
        curr (obj): object of curser class
        conn (obj): connection object 
        
    Returns:
        no return values
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """    
    - Establishes connection to the redshift cluster using configtration data in dwh.cfg and gets
      cursor to it.
    - Drops all tables if exist.  
    - Creates needed tables (staging tables and star schema tables). 
    - Finally, closes the connection. 
    Args:
        no args
        
    Returns:
        no return values
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
