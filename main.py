from flask import Flask,request, render_template,redirect,url_for
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "flask"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Kgisl@123"
app.config['MYSQL_CURSORCLASS']="DictCursor"
app.secret_key="myapp"

conn = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def signin():
    if request.method  == 'POST':
        user_name1 = request.form['user_name']
        password1 = request.form['password']
        con=conn.connection.cursor()
        sql = "select user_name, password from 21_04_2023 WHERE user_name= %s and  password=%s"
        result=con.execute(sql,(user_name1,password1))
        con.connection.commit()
        con.close()
        
        if result:
            return redirect(url_for('addrbook1'))
        else:
            return render_template('signin_op.html')
            
        
    return render_template('signin.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method  == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        con=conn.connection.cursor()
        sql = "insert into 21_04_2023(user_name,password) values  (%s,%s)"
        result=con.execute(sql,(user_name,password))
        con.connection.commit()
        con.close()
        return  f'Welocme {user_name} Signin to continue'
        
    return render_template('signup.html')


@app.route('/add/', methods = ['POST', 'GET'])
def add():
    if request.method  == 'POST':
        name = request.form['name']
        watsapp_no = request.form['watsapp_no']
        door_no = request.form['door_no']
        street = request.form['street']
        city = request.form['city']
        pincode = request.form['pincode']
        con=conn.connection.cursor()
        sql = "insert into addrbook(name,watsapp_no,door_no,street,city,pincode) values  (%s,%s,%s,%s,%s,%s)"
        result=con.execute(sql,(name,watsapp_no,door_no,street,city,pincode))
        con.connection.commit()
        con.close()
        return  f' {name} Address Details Added Successfully'
        
    return render_template('add.html')
        
                                                                                                                                                                        
@app.route('/addrbook1/',methods=['GET', 'POST'])
def addrbook1():
    con=conn.connection.cursor()
    sql="select * from  addrbook"
    con.execute(sql)
    result= con.fetchall()
    con.connection.commit()    
    return render_template('addrbook1.html',rows=result)
    
    
@app.route('/add1/',methods=['GET', 'POST'])
def add1(): 
    return render_template('add.html')
        
@app.route('/search/',methods=['GET', 'POST'])
def search(): 
    return render_template('search.html')
    

 
 
if __name__ =='__main__':
    app.run(debug=True)