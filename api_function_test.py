from app import app  
from flask import  request,jsonify

@app.route('/test',methods=['GET','POST'])  
def test(): 
    if request.method == 'GET':  
        #response of api in /test route
        return jsonify({'response':'Get Request Called now'}) 
    elif request.method =='POST': 
        req_Json = request.json 
        name = req_Json['name']  
        #repsonse of api in /test route
        return jsonify({'response':'hi'+name})  

if __name__ == '__main__': 
    app.run(debug=True,port=5000) 

