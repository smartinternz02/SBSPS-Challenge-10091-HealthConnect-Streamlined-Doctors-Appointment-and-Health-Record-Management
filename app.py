from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
        
def insertdb(conn,department,doctor,date,time,name,phonenumber,email,whats,problem):
    sql= "INSERT into APPOINTMENT VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(department,doctor,date,time,name,phonenumber,email,whats,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ttc49708;PWD=tgDPXxdv4cUP06PS",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply0')
def apply0():
    return render_template('index.html')

@app.route('/apply1')
def apply1():
    return render_template('about.html')

@app.route('/apply2')
def apply2():
    return render_template('service.html')

@app.route('/apply3')
def apply3():
    return render_template('department.html')

@app.route('/apply4')
def apply4():
    return render_template('doctor.html')

@app.route('/apply5')
def apply5():
    return render_template('contact.html')

@app.route('/apply6')
def apply6():
    return render_template('appoinment.html')



@app.route('/make', methods=['POST','GET'])
def make():
    if request.method == "POST":
        department = request.form['department']
        doctor = request.form['doctor']
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        phonenumber = request.form['phonenumber']
        email = request.form['email']
        whats = request.form['whatsappno']
        problem = request.form['problem']
        insertdb(conn,department,doctor,date,time,name,phonenumber,email,whats,problem)
        return render_template('confirmation.html')
        




if __name__ =='__main__':
    app.run( debug = True)
