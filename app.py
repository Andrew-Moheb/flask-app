import sqlite3
from flask import Flask,  render_template, request, redirect
app = Flask(__name__) 


@app.route("/", methods=['GET','POST'])  
def index():  
    if  request.method == 'POST':   

#sqlite 
        connection = sqlite3.connect   ('users_data.db')  
        cursor = connection.cursor()  
#html form  
        name = request.form['name']
        password = request.form['password']     

#query  
        query = "SELECT name,password FROM users where name='"+name+"' and password='"+password+"'" 
        cursor.execute(query) 
        results = cursor.fetchall()  

#validation  
        if len(results) == 0: 
            return render_template('Failure.html') 
        else:
            return render_template('loged_in.html')
      
#html
    return render_template('index.html') 
 

