from flask import Flask, jsonify, request, render_template
import mysql.connector
from flask_cors import CORS
from mydatabase import *
from QueryInsert import *
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/submit', methods=['POST'])
# def submit():
#     data = request.json
#     selected_options = data.get('selectedOptions')
#     # 处理选中的选项
#     return jsonify(success=True)

@app.route('/api/query', methods=['POST'])
def get_data():
    try:
              
        data = request.json
        print(data)

        versions = data.get('version')
        scenes = data.get('scene')
        startDate = data.get('startDate')
        endDate = data.get('endDate')[:10]

        metrics = data.get('metrics')[:10]

        results,col_name = my.query_record(versions,scenes,metrics,startDate,endDate)
        print(results,col_name)
        js = jsonify({'result': results,
                      "col_name":col_name})
        # print(js,data)
        return js
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return

@app.route('/api/insert', methods=['POST'])
def insert_data():
    try:
        
        
        data = request.json
        print(data)

        version = data.get('version')
        
        date = data.get('date')[:10]
        print(date)
        taskid = data.get('task_id')
        info = deal_one_task(my,version,date,taskid)
        # results,col_name = my.query_record(versions,scenes,metrics,dates)
        # print(results,col_name)
        js = jsonify({'info': info}
                      )
        # print(js,data)
        return js
    except Exception as err:
        print(f"Error: {err}")
        return
    
if __name__ == '__main__':
    
    my = MyDatabase(host="localhost",
    user="root",
    password="123456",
    database="hil_db")
    my.connect()

    app.run(debug=True)
