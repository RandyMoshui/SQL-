import pyodbc


class ODBC:
    def __init__(self, server, uid, pwd, db, DRIVER='{SQL Server}'):
        self.server = server
        self.uid = uid
        self.pwd = pwd
        self.db = db
        self.DRIVER = DRIVER

    def GetConnect(self):
        if not self.db:
            raise (NameError, '没有设置数据库信息')
        self.conn = pyodbc.connect(SERVER=self.server, UID=self.uid, PWD=self.pwd, DATABASE=self.db, DRIVER=self.DRIVER)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, '连接数据库失败')
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def main():
    ms = ODBC(server='localhost', uid='sa', pwd='zjh5729.', db="online_course")
    sql = ms.ExecQuery('SELECT * from Users where id=201983290527')
    print(type(sql[0][0]))
    print(sql[0][2])
    print(len(sql))





if __name__ == '__main__':
    main()