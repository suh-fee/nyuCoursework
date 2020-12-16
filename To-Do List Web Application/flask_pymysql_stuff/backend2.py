from flask import Flask, render_template, jsonify, request, session
import pymysql

app = Flask(__name__)

# index page
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ha1sa0ni', db='todo_database') # INSERT YOUR PASSWORD TO DATABASE HERE
    todo_list = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT TEXT from Todos") # selects all items from table
        todo_list = [item[0] for item in cur]
    finally:
        cur.close()
        conn.close()
    return render_template('front.html', todo_list=todo_list)
    
# read page
@app.route('/todo/read', methods=['GET'])
def all_items():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ha1sa0ni', db='todo_database') # INSERT YOUR PASSWORD TO DATABASE HERE
    todo_list = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT TEXT from Todos") # selects all items from table
        todo_list = [item[0] for item in cur]
    finally:
        cur.close()
        conn.close()
    return jsonify({"result":"succes", "data":todo_list})
    
# create new item
@app.route('/todo/create', methods=['POST'])
def new_item():
    data = request.get_json() # request is in json form
    item = data['content'] # gets item name
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ha1sa0ni', db='todo_database') # INSERT YOUR PASSWORD TO DATABASE HERE
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO Todos (TEXT) VALUES ('{}')".format(item)) # inserts to table , ID increments automatically, TEXT is item name
        conn.commit()
    finally:
        cur.close()
        conn.close()
    return jsonify({"result":"succes"})

# update item 
@app.route('/todo/update', methods=['PUT'])
def update_item():
    data = request.get_json()
    index = int(data['item_number']) # gets item number (li position in ul on web page)
    item = data['content']
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ha1sa0ni', db='todo_database') # INSERT YOUR PASSWORD TO DATABASE HERE
    try:
        cur = conn.cursor()
        cur.execute("UPDATE Todos SET TEXT = '{}' WHERE ID = {}".format(item, index+1)) # updates table, we need to increment index + 1 because we are indexing from 0 and mysql from 1
        conn.commit()
    finally:
        cur.close()
        conn.close()
    return jsonify({"result":"succes"})

# delete item
@app.route('/todo/delete', methods=['DELETE'])
def delete_item():   
    data = request.get_json()
    index = int(data['item'])
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ha1sa0ni', db='todo_database')
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Todos WHERE ID = {}".format(index+1)) # deletes item from table, again index + 1 because mysql is indexing from 1
        conn.commit()
        cur.execute("UPDATE Todos SET ID = ID - 1 WHERE ID > {}".format(index+1)) # decrements all indexes that are higher than the one that was deleted
        conn.commit()
        cur.execute("SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'todo_database' AND TABLE_NAME = 'Todos'") # gets AUTO_INCREMENT value
        oldIncrement = [item[0] for item in cur][0]
        cur.execute("ALTER TABLE Todos AUTO_INCREMENT = {}".format(oldIncrement-1)) # sets auto increment so it will increment IDs from correct value after deleting some item
        conn.commit()
    finally:
        cur.close()
        conn.close()   
    return jsonify({"result":"succes"})
    


if __name__ == "__main__":
    app.run(debug=True)