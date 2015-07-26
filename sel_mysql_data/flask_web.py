#coding=utf8
from flask import Flask,request,render_template,session,url_for,redirect
import MySQLdb as mysql
import json

app=Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chart_data')
def chart_data():
    m=[]
    m.append(['PE','CMF'])
    m.append({'value':200,'name':'PE'})
    m.append({'value':30,'name':'cmf'})
    print m
    o={}
    o['DBNAME']=m[0]
    o['data']=m[1:]
    o['t']=123
    print json.dumps(o)
    return json.dumps(o)


@app.route('/chart_data2')
def chart_data2():
    m=[]
    m.append(['PE','CMF'])
    m.append({'value':200,'name':'PE'})
    m.append({'value':30,'name':'cmf'})
    print m
    o={}
    o['DBNAME']=m[0]
    o['data']=m[1:]
    o['t']=456
    print json.dumps(o)
    return json.dumps(o)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=33516,debug=True)
