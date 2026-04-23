import pymysql
connn=pymysql.connect(host='localhost',user='Arshad',password='root')
print('connnected')
cur=connn.cursor()
cur.execute('use day1')
cur.execute('select * from schooling')
tables=cur.fetchall()
for x in tables:
    print(x)