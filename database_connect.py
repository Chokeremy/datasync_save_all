import psycopg2


class DatabaseConnect:

    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()

    def get_data(self, sql):
        self.cursor.execute(sql)
        data_list = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return data_list
