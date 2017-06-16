#!/usr/bin/env python

from flask import Flask
import memcache
import MySQLdb
import redis

mysql = MySQLdb.connect(host="127.0.0.1", user="root")
arcus = memcache.Client(["127.0.0.1:11211"])
#nbase = redis.StrictRedis(host="localhost", port=
app = Flask(__name__)

@app.route("/mysql")
def mysql():
    pass

@app.route("/arcus")
def arcus():
    pass

@app.route("/nbase")
def nbase():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0")
