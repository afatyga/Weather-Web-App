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
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)


@app.route('/')
def root2():
    temp = []

    with db.connect() as conn:
        all_data = conn.execute("SELECT * FROM entries;").fetchall()
        for row in all_data:
            temp.append(row[0])
    return render_template(
        'mainpage.html', temp=temp)


@app.route('/geo')
def geo():
    return render_template('geolocation.html')

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
