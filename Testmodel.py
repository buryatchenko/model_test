import sqlite3
class Testmodel:
    def __init__(self):
        self._connect = sqlite3.connect('heal.db')
        self._cursor = self._connect.cursor()

    def insert_dates(self, name, Reception, Price, Datatime):
        sql='''INSERT INTO heal (name, Reception, Price, Datatime) VALUES (?, ?, ?, ?)'''
        self._cursor.execute(sql, [name, Reception, Price, Datatime])
        self._connect.commit()
			
    def data_table(self):
        sql = '''SELECT name, Reception, Price, Datatime  FROM  heal'''
        tb = []
        for row in self._cursor.execute(sql):
            r = []
            for v in row:
                r.append(v)
            tb.append(r)
        return tb