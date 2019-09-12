from flask import Flask, render_template, Response, request

from flask_sqlalchemy import SQLAlchemy
import logging
logging.basicConfig(level=logging.INFO)

import sqlalchemy

app = Flask(__name__)
import os

db_user = "root"
db_pass = "47"
db_name = "sensorData" #database it's reading from!
cloud_sql_connection_name = "ec463-group47:northamerica-northeast1:instance"


db = sqlalchemy.create_engine(
    # Equivalent URL:
    #mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
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
#write random values into 2 lists
#with db.connect() as conn:
#    conn.execute(
#            "CREATE TABLE entries2 (temp INTEGER, humidity DECIMAL(1,2));"
#            "INSERT INTO entries2 (temp, humidity) values "
#            "( vote_id SERIAL NOT NULL, time_cast timestamp NOT NULL, "
 #           "candidate CHAR(6) NOT NULL, PRIMARY KEY (vote_id) );"
  #      )


@app.route('/')
def root():
	temp = []
	humidity = []
	with db.connect() as conn:
        # Execute the query and fetch all results
		all_data = conn.execute(
            "SELECT * FROM entries;"
		).fetchall()
        # Convert the results into a list of dicts representing votes
		for row in all_data:
			temp.append(row[0])
			humidity.append(row[1])
            #data.append('temp': row[0],'humidity': row[1])
	return render_template('mainpage.html', temp = temp, humidity = humidity, length = len(temp))

@app.route('/temp')
def temp():
	temper = []
	humid = []
	with db.connect() as conn:
        # Execute the query and fetch all results
		all_data = conn.execute("SELECT * FROM entries;").fetchall()
        # Convert the results into a list of dicts representing votes
		for row in all_data:
			temper.append(row[0])
			humid.append(row[1])
            #data.append('temp': row[0],'humidity': row[1])
	length = len(temper)
	return render_template(
        'temptest.html', temper =temper, humidity = humid, length = length)

@app.route('/location')
def location():
    return render_template(
        'location.html')

if __name__ == '__main__':

    app.run()
