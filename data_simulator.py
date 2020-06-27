import mysql.connector as sql
import random
from time import sleep


def simulator(data, header_id):
    try:
        conn = sql.connect(user='root', password='Son@123456',
                                host='localhost', database='miniproject')
        cursor = conn.cursor()
    except sql.Error as err:
        if err.errno == sql.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == sql.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    #print("testing: ", dir(cursor))
    query = """
        INSERT INTO sensor_data (data_value, sensor_header_id) VALUES (%s, %s)
    """
    val = (data, header_id)
    try:
        cursor.execute(query, val)
        conn.commit()
    except sql.Error as err:
        print(err)

def main():
    humidity_range = []
    for i in range(15,27):
        humidity_range.append(i)
    print(humidity_range)
    tmp_range = []
    for i in range(20,45):
        tmp_range.append(i)
    print(tmp_range)
    light_range = []
    for i in range(0,100):
        light_range.append(i)
    print(light_range)
    i=1
    while i<11:
        print("Updating sensors data")
        humidity = random.choice(humidity_range)
        simulator(humidity, 1)
        temp = random.choice(tmp_range)
        simulator(temp, 2)
        light = random.choice(light_range)
        simulator(light, 3)
        humidity = random.choice(humidity_range)
        simulator(humidity, 4)
        temp = random.choice(tmp_range)
        simulator(temp, 5)
        light = random.choice(light_range)
        simulator(light, 6)
        humidity = random.choice(humidity_range)
        simulator(humidity, 7)
        temp = random.choice(tmp_range)
        simulator(temp, 8)
        light = random.choice(light_range)
        simulator(light, 9)

        sleep(30)
        i=i+1    

if __name__=="__main__":
    main()
    pass
