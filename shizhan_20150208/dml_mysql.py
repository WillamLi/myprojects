#coding=utf8
from flask import Flask,request,render_template,session,url_for,redirect
import MySQLdb as mysql
import json

app=Flask(__name__)

con=mysql.connect(user='reboot',passwd='reboot123',db='lr',charset='utf8')
#db.autocommit(True)
cur=con.cursor()

def czdb(name,ip):
    con=mysql.connect(user='reboot',passwd='reboot123',db='lr',charset='utf8')
    cur=con.cursor()

    sql="insert into cmdb_test(name,ip) values('%s','%s')"
    cur.execute(sql%(name,ip))


@app.route('/t')
def t():
    if 'username' in session:
	return 'hello admin your list is xxx'
    else:
	return 'you are not log in'


@app.route('/login')
def login():
    user=request.args.get('username')
    if not user:
	return 'need a user name'
    if user=='admin':
	session['username']=user
#	return 'success'
	return redirect('t')
    else:
	return 'invalid user'




#捕获添加
@app.route('/add',methods=["GET"])
def dmlmysql():
    return_dict={'errno':1,'msg':''}
    if not request.args.get('name'):
#	return '请输入name'
	return_dict['msg']='need a name'
	return json.dumps(return_dict)
    if not request.args.get('ip'):
#	return '请输入ip'
	return_dict['msg']='need a ip'
	return json.dumps(return_dict)
    name=request.args.get('name')
    ip=request.args.get('ip')

    czdb(name,ip)
#    return 'Success'
    return_dict['errno']=0
    return json.dumps(return_dict)

#    con=mysql.connect(user='reboot',passwd='reboot123',db='lr',charset='utf8')
#    cur=con.cursor()

#    sql="insert into cmdb_test(name,ip) values('%s','%s')"
#    cur.execute(sql%(name,ip))
#    return 'Success'



@app.route('/',methods=["GET"])
def cz1():
    return render_template('dml.html')

@app.route('/list',methods=["GET"])
def list():
    sql="select * from cmdb_test"
    str = ''
    cur.execute(sql)
    for c in cur.fetchall():
#        s='<tr><td>%s</td><td>%s</td><td>%s</td><td><span class="delete-btn" data-id="%s">delete</span></td></tr>' % (c[0],c[1],c[2],c[0])
        s='<tr><td>%s</td><td>%s</td><td>%s</td><td><button class="delete-btn" data-id="%s">delete</button></td><td><button class="update-btn" up-id="%s">update</button></td></tr>' % (c[0],c[1],c[2],c[0],c[0])
        str +=s
    return str


#捕获删除
@app.route('/delete')
def delete():
    id=request.args.get('id')
    if not id:
	return 'need an id'
    sql="delete from cmdb_test where id=%s" %(id)
    cur.execute(sql)
    return 'success'


#@app.route('/update')
#def update():
#    id=request.args.get('id')
#    if not id:
#	return 'need an id'
#    sql="update cmdb_test set name=%s,ip=%s" %(name,ip)
#    cur.execute(sql)
#    return 'success'

#捕获更新时先查询
@app.route('/upsel')
def upsel():
    return_dict={'errno':1,'msg':''} 
    id=request.args.get('id')
    if not id:
	return_dict['msg']='need a id' 
	return json.dumps(return_dict)
    sql="select * from cmdb_test where id=%s" %(id)
    cur.execute(sql)
    re_dict={}
    res=cur.fetchone()
    re_dict['id']=res[0]
    re_dict['name']=res[1]
    re_dict['ip']=res[2]
#    return re_dict
    return json.dumps(re_dict)
#    for c in cur.fetchall():
#        return_upseldict="'id':'%s','name':'%s','ip':'%s'"  %(c[0],c[1],c[2])
#        return return_upseldict
#        return json.dumps(return_upseldict)

#更新操作
@app.route('/update')
def update():
    return_dict={'errno':1,'msg':''}
    id=request.args.get('id')
    if not id:
	return_dict['msg']='need a id'
	return json.dumps(return_dict)
    name=request.args.get('name')
    if not name:
	return_dict['msg']='need a name'
   	return json.dumps(return_dict)
    ip=request.args.get('ip')
    if not ip:
	return_dict['msg']='need a ip'
	return json.dumps(return_dict)
    print name,ip,id
    sql="update cmdb_test set name='%s',ip='%s' where id=%s" %(name,ip,id)
#    sql="update cmdb_test set ip='%s' where name='%s'" %(ip,name)
#    id=request.args.get('id')
#    name=request.args.get('name')
#    ip=request.args.get('ip')
    print sql
    cur.execute(sql)
    return_dict['errno']=0
    print return_dict
    return json.dumps(return_dict)


@app.route('/chart')
def chart():
    return render_template('chart.html')
@app.route('/chart_data')
def chart_data():
    o={}
    o['catg']=['one','two','three']
    o['data']=[]
    o['data'].append({'name':'wd','data':[20,30,25]})
    o['data'].append({'name':'pc','data':[100,90,120]})
    print json.dumps(o)
    return json.dumps(o)



######
@app.route('/xiala',methods=['GET'])
def xiala():
    return render_template('xialakuang.html')

@app.route('/sldata')
def xld():
    sql="select id,name from host"
    str=''
    cur.execute(sql)
    for c in cur.fetchall():
	 print c
	 s='<option value="%d">%s</option>' %(c[0],c[1])
         str+=s
    return  str

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9119,debug=True)
#    app.run(host='0.0.0.0',port=9119)
