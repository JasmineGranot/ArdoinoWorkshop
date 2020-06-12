import mysql.connector
from server_side import Const
import pandas as pd


class DBHandler:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='workshop', password='ws4@MTA',
                                           host=Const.DB_IP,
                                           database='workshop')

    def __del__(self):
        self.cnx.close()

    def getData(self, query):
        return pd.read_sql_query(query, self.cnx)

    def execute(self, query):
        cur = self.cnx.cursor()
        cur.execute(query)
        self.cnx.commit()
