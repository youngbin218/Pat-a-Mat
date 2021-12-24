class Connection:
    def __init__(self):
        self.fruit_Name = []
        self.freshness_Standard = []
        self.order_History = []
    
    def select():
        conn = pymysql.connect(host='localhost', user='root', password='password', db='developer', charset='utf8') 

        cursor = conn.cursor() 

        sql = "SELECT * FROM user where department = %s" 

        cursor.execute(sql, ("AI")) 
        res = cursor.fetchall() 

        for data in res: 
            print(data) 

        conn.commit() 
        conn.close()
    
    def getFruitName():
        return self.fruit_Name
    
    def getFreshnessStandard():
        return self.freshness_Standard
    
    def getOrderHistory():
        return self.order_History
