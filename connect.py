from flask import Flask, render_template, request,session

import ibm_db

def showall():
    sql = "SELECT * from APPOINTMENT"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The department is : ",  dictionary["DEPARTMENT"])
        print("The doctor is : ", dictionary["DOCTOR"])
        print("The date is : ",  dictionary["DATE"])
        print("The time is : ",  dictionary["TIME"])
        print("The fullname is : ",  dictionary["Full name"])
        print("The Phonenumber is : ",  dictionary["PHONENUMBER"])
        print("The Problem is : ",  dictionary["EMAIL"])
        print("The Problem is : ",  dictionary["WHATSAPPNUMBER"])
        print("The Problem is : ",  dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)

def insert_db(conn, DEPARTMENT,DOCTOR, DATE, TIME, Fullname,PHONENUMBER,EMAIL,WHATSAPPNUMBER,PROBLEM):
    sql = "INSERT into APPOINTMENT VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}' , '{}' , '{}')".format(DEPARTMENT,DOCTOR, DATE, TIME, Fullname,PHONENUMBER,EMAIL,WHATSAPPNUMBER,PROBLEM)
    stmt = ibm_db.exec_immediate(conn, sql)
    print("Number of affected rows: ", ibm_db.num_rows(stmt))

    

try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ttc49708;PWD=tgDPXxdv4cUP06PS", '', '')
    print(conn)
    print("Connection successful...")
    
    # Call the function to show all records
    showall()
 # Example of inserting a new record
    insert_db(conn, "Cardiology", "Dr. Smith", "2023-08-26", "10:00 AM", "John Doe", "1234567890","karthik@gmail.com","4567891230","Heart issues")
    
   

except Exception as e:
    print("Error connecting to the database:", e)
