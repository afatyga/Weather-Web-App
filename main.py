from flask import Flask, render_template, Response, request

from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.INFO)

import sqlalchemy

from random import *

app = Flask(__name__)
import os

db_user = "root"
db_pass = "47"
db_name = "sensorData"  # database it's reading from!
cloud_sql_connection_name = "ec463-group47:northamerica-northeast1:instance"

db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    ),
    pool_size=5,
    max_overflow=2,

    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes

)


# write random values into 2 lists
# x = []
# y = []
# z = []
# for i in range(10):
#	a = randint(1, 100)
#	b = randint(1,100)
#	x.append(a/100)
#	y.append(b)
#	#z.append((a,b))

# with db.connect() as conn: #how to create a new table within the database
#    conn.execute(
#            "CREATE TABLE entries2 (temp INTEGER, humidity DECIMAL(3,2));"
#        )
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[0] + "," + y[0] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[1] + "," + y[1] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[2] + "," + y[2] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[3] + "," + y[3] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[4] + "," + y[4] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[5] + "," + y[5] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[6] + "," + y[6] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[7] + "," + y[7] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[8] + "," + y[8] + ");")
#    conn.execute("INSERT INTO entries2(temp,humidity) VALUES(" + x[9] + "," + y[9] + ");")


#@app.route('/')
#def root():
   # temp = []
   # humidity = []
   # data = []
   # with db.connect() as conn:
      #  all_data = conn.execute(
     #       "SELECT * FROM entries;"
    #    ).fetchall()
   #     for row in all_data:
  #          temp.append(row[0])
 #           humidity.append(row[1])
    #   data.append({'x': row[0],'y': row[1]})
#    return render_template('mainpage.html', temp=temp, humidity=humidity, length=len(temp))


@app.route('/')
def temp():
    temper = []
    humid = []
    data = []
    with db.connect() as conn:
        all_data = conn.execute("SELECT * FROM entries;").fetchall()
        for row in all_data:
            temper.append(row[0])
            humid.append(row[1])
            data.append({'x': row[0], 'y': row[1]})
    length = len(temper)
    return render_template(
        'mainpage.html', temp=temp, humidity=humidity, length=length, data=data)


@app.route('/location')
def location():
    return render_template(
        'location.html')


if __name__ == '__main__':
    app.run()
