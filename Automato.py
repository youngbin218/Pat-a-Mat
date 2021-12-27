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
    
    
class OrderManagement():
    def __init__(self, order_List):
        self.order_List = order_List
        self.sleep_Queue = []
        self.run_Queue = []
        self.change = {1:False, 2:False, 3:False}

    def sleepQueue(self):
        for element in self.order_List:
            self.sleep_Queue.append(element)

    def runQueue(self, num=0, port=0):
        if len(self.sleep_Queue) == 0:
            print('No more order')
            return

        if port == 0:
            for i in range(num):
                #del(self.sleep_Queue[0]['OrderNumber'])
                self.run_Queue.append(self.sleep_Queue[0])
                self.sleep_Queue = self.sleep_Queue[1:]
        else:
            del(self.run_Queue[port-1])
            #del(self.sleep_Queue[0]['OrderNumber'])
            self.run_Queue.insert(port-1, self.sleep_Queue[0])
            self.sleep_Queue = self.sleep_Queue[1:]
    def checkPackage(self, port):
        self.change[port] = True

    def getRunQueue(self):
        return self.run_Queue


'''class Model():
    def runModel(self):
        Turn on camera
        use TensorRT

    def result(self):
        receive detect value
        return fruit_Detect'''


class Status():
    def __init__(self, fruit_Detect, fruit_Name, run_Queue):
        self.fruit_Detect = fruit_Detect
        self.fruit_Name = fruit_Name
        self.run_Queue = run_Queue
        self.is_Fresh = False
        self.in_Order = False

    def checkFreshness(self):
        if self.fruit_Detect in self.fruit_Name:
            self.is_Fresh = True

    def checkOrderList(self):
        if self.is_Fresh:
            for i in range(3):
                if self.run_Queue[i][str(self.fruit_Detect)] > 0:
                    self.in_Order = True
                    break

    def getStatus(self):
        return self.is_Fresh, self.in_Order


class Distribution():
    def __init__(self, fruit_Detect, run_Queue):
        self.fruit_Detect = fruit_Detect
        self.run_Queue = run_Queue
        self.prior= {1 : 0, 2 : 0, 3 : 0}

    def plusPrior(self, port):
        self.prior[port-1] += 1

    def scheduling(self):
        # Find order that contain fruit_Detect
        # Scheduling
        # In case, use Aging(priority)
        for i in range(3):
            if self.run_Queue[i][str(self.fruit_Detect)] > 0:
                self.check.append(i)

        for ele in check:
            if self.prior[ele] > 3:
                self.consider_Priority.append(ele)

        if len(consider_Priority) > 1:



        elif len(consider_Priority) == 1:
            self.prior[consider_Priority[0]] = 0
            self.run_Queue[consider_Priority[0]+1][str(self.fruit_Detect)] -= 1

            return consider_Priority[0]+1

        else:

    def decidePort(self, is_Fresh, in_Order):
        if is_Fresh == False:
            return 4
        elif is_Fresh == True and in_Order == False:
            return 5
        elif is_Fresh == True and in_Order == True:
            port, run_Queue = scheduling()
            return port

    def getRunQueue(self):
        return self.run_Queue

    
import pymysql

def main():
    # Connect Database and Receive Info
    conn = Connection()
    conn.select()
    fruit_Name = conn.getFruitName()
    order_List = conn.getOrderList()

    # Manage sleepQueue and runQueue
    orde = OrderManagement(order_List)
    orde.sleepQueue()
    orde.runQueue(3)
    run_Queue = orde.getRunQueue()
    print(run_Queue)

    #while (len(run_Queue) != 0) {

    # Run Light-YOLOv4
    #mod = Model()
    #fruit_Detect = result()
    fruit_Detect = 'rotten'

    # Check Object's Status
    st = Status(fruit_Detect, fruit_Name, run_Queue)
    st.checkFreshness()
    st.checkOrderList()
    is_Fresh, in_Order = st.getStatus()
    run_Queue = st.getRunQueue()

    # Consider Priority and Decide Port Number
    dis = Distribution(fruit_Detect, run_Queue)
    port = dis.decidePort(is_Fresh, in_Order)
    print(port)

if __name__ == '__main__':
    main()
