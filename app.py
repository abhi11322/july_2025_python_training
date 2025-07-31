from flask import Flask,jsonify,request,render_template
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'abhishek_cse'
 
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/myname/<name>')
def y_name(name):
    return jsonify({'message':"hello","name":name })

@app.route('/login', methods = ['POST', 'GET'])
def login():
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO user(name,email,password) VALUES(%s,%s,%s)''',("robert","robert@gamil.com","pass8"))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
@app.route('/name', methods = [ 'GET'])
def getname():
       name= request.args.get("name")
       return name

@app.route('/form', methods = [ 'GET','POST'])
def getform():
          if request.method == "GET":
            return render_template('form.html')
          else: 
                id=request.form.get("id")
                name=request.form.get("name")
                email=request.form.get("email")
                password=request.form.get('password') 
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO user(id,name,email,password) VALUES(%s,%s,%s,%s)",[id,name,email,password])
                mysql.connection.commit()
                cursor.close()    
                return "save"
          
@app.route('/getdata')
def getdata():
      id=request.args.get("id")
      sql=''
      if id :
            sql=f"select * from user where id = {id}"
      else:
            sql="select * from user"
        
      cur = mysql.connection.cursor()
      cur.execute(sql)
      result=cur.fetchall()
     
      mysql.connection.commit()
      cur.close()
      return jsonify(result)

@app.route('/getdatainHtml')
def getdatainHtml():
      id=request.args.get("id")
      sql=''
      if id :
            sql=f"select * from user where id = {id}"
      else:
            sql="select * from user"
        
      cur = mysql.connection.cursor()
      cur.execute(sql)
      result=cur.fetchall()
     
      mysql.connection.commit()
      cur.close()
      return render_template('userlist.html',userlist=result)

@app.route('/userdetail')
def userDetail():
      id=request.args.get("id")
      sql=f"select * from user where id = {id}"
      cur = mysql.connection.cursor()
      cur.execute(sql)
      result=cur.fetchall()
     
      mysql.connection.commit()
      print(result)
      cur.close()

      return render_template("userdetail.html",
                             id=result[0][0],
                             name=result[0][1],
                             email=result[0][2])

if __name__=='__main__':
    app.run()


