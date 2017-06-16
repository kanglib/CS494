#!/usr/bin/env python

from flask import Flask
import memcache
import MySQLdb
import random
import redis

mysql = MySQLdb.connect(host="127.0.0.1", user="root")
arcus = memcache.Client(["127.0.0.1:11211"])
nbase = redis.StrictRedis(port=6000)

mysql.query("DROP DATABASE arcus;")
mysql.store_result()
mysql.query("CREATE DATABASE arcus;")
mysql.store_result()
mysql.query("USE arcus;")
mysql.store_result()
mysql.query("CREATE TABLE cs494 (dept VARCHAR(100), sid INTEGER PRIMARY KEY, name VARCHAR(100));")
mysql.store_result()

for i in range(8000):
    dept = random.choice(["Mechanical Engineering", "Electrical Engineering", "School of Computing..."])
    sid = 20170001 + i
    name = random.choice(["In", "Kim", "Jun"]) + " " + random.choice(["Gigye", "Jeonja", "Sani"])
    mysql.query("INSERT INTO cs494 VALUES ('%s', %d, '%s');" % (dept, sid, name))
    mysql.store_result()

def query(sid):
    mysql.query("SELECT * FROM cs494 WHERE sid=%d LIMIT 1;" % sid);
    return `mysql.store_result().fetch_row(1)`

app = Flask(__name__)

@app.route("/mysql")
def get_mysql():
    k = random.randint(20170001, 20170400)
    v = query(k)
    return v

@app.route("/arcus")
def get_arcus():
    k = random.randint(20170001, 20170400)
    v = arcus.get("cs494:%d" % k)
    if v:
        return "Hit: %s" % v
    v = query(k)
    arcus.set("cs494:%d" % k, v)
    return "Miss: %s" % v

@app.route("/nbase")
def get_nbase():
    k = random.randint(20170001, 20170400)
    v = nbase.get("cs494:%d" % k)
    if v:
        return "Hit: %s" % v
    v = query(k)
    nbase.set("cs494:%d" % k, v)
    return "Miss: %s" % v

if __name__ == "__main__":
    app.run(host="0.0.0.0")
