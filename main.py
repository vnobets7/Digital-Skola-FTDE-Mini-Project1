import os
import connection
import sqlparse
import pandas as pd

if __name__ == '__main__':
    # connection data source
    conf = connection.config('marketplace_prod')
    conn, engine = connection.get_conn(conf, 'DataSource')
    cursor = conn.cursor()
    
    # connection dwh
    conf_dwh = connection.config('dwh')
    conn_dwh, engine_dwh = connection.get_conn(conf_dwh, 'DWH')
    cursor_dwh = conn.cursor()
