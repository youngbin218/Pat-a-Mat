class Connection:
    def __init__(self):
        self.fruit_Info = {}
        self.order_List = []

    def select(self):
        conn = pymysql.connect(host='localhost', user='root', password='automato', db='capstone', charset='utf8')

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql_fruit = "SELECT * FROM `Fruit`;"
        sql_list = "SELECT * FROM `List`;"

        cursor.execute(sql_fruit)
        res = cursor.fetchall()

        for data in res:
            tmp = list(data.values())
            self.fruit_Info[str(tmp[0])] = tmp[1]

        cursor.execute(sql_list)
        res = cursor.fetchall()

        for data in res:
            self.order_List.append(data)

        conn.commit()
        conn.close()

    def getFruitInfo(self):
        return self.fruit_Info
    
    def getOrderList(self):
        return self.order_List

import pymysql

conn = Connection()
conn.select()
fruit_Info = conn.getFruitInfo()
order_List = conn.getOrderList()
