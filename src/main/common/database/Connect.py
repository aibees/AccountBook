from common.util.Config import Config
import pymysql


class Connection:
    def __init__(self):
        self.conf = Config()
        self.conn = None
        self.connection()

    def connection(self):
        self.conn = pymysql.connect(
            host=self.conf.getConfig("DATABASE", "DB_HOST")
            , user=self.conf.getConfig("DATABASE", "DB_USER")
            , port=3306
            , passwd=self.conf.getConfig("DATABASE", "DB_PSWD")
            , db=self.conf.getConfig("DATABASE", "DB_SCHM")
            , charset='utf8'
            , cursorclass=pymysql.cursors.DictCursor
        )

    def select(self, sql, params):
        return self.__fetch(sql, params)

    def __fetch(self, sql, params):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)

        return cursor.fetchall()

    def insert(self, sql, params):
        self.__execute(sql, params)

    def __execute(self, sql, params):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        self.conn.commit()
