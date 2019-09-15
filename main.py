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

db = sqlalchemy.create_engine( #creating a connection to the database tha can be used
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
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)


@app.route('/') #creates the flask html route
def root():
    temp = []
    with db.connect() as conn: #this is connecting to the database to fetch data from it
        all_data = conn.execute("SELECT * FROM entries;").fetchall() #sql command being executed and then fetch on that
        for row in all_data:
            temp.append(row[0]) #adding to the temp list
    return render_template(
        'mainpage.html', temp=temp)

    return render_template('test.html')


if __name__ == '__main__':
    app.run()
