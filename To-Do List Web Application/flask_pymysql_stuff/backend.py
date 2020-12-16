from flask import Flask, render_template, jsonify, request, session


app = Flask(__name__)
app.secret_key = "YouWillNeverGuessThisSuperSecretKey"

todo_list = [] # list variable

# index page
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    return render_template('front.html', todo_list=todo_list)
    
# read page
@app.route('/todo/read', methods=['GET'])
def all_items():
    return jsonify({"result":"succes", "data":todo_list})
    
# create new item
@app.route('/todo/create', methods=['POST'])
def new_item():
    data = request.get_json()
    item = data['content'] # gets item name from json
    todo_list.append(item) # appends item to list
    return jsonify({"result":"succes"})

# update page    
@app.route('/todo/update', methods=['PUT'])
def update_item():
    data = request.get_json()
    index = int(data['item_number']) # gets index of item
    item = data['content'] # new value of item
    if index > len(todo_list)-1:
        return jsonify({"result":"fail"})
    todo_list[index] = item # updates item on the right index
    return jsonify({"result":"succes"})

# delete page
@app.route('/todo/delete', methods=['DELETE'])
def delete_item():   
    data = request.get_json()
    index = int(data['item'])
    if index > len(todo_list)-1:
        return jsonify({"result":"fail"})
    del todo_list[index]
    return jsonify({"result":"succes"})
    


if __name__ == "__main__":
    app.run(debug=True)
    