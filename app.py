from flask import Flask,request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""

    html = """<table border="1px">
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Type</th>
    </tr>
    """

    data = db.all()
    for i in data:
        name = i['name']
        quantity = i['quantity']
        price = i['price']
        type_1 = i['type']

        row = f"""<tr>
                    <td>{name}</td>
                    <td>{quantity}</td>
                    <td>{price}</td>
                    <td>{type_1}</td>
                 </tr>"""
        
        html += row
    
    html += "</table>"

    return html
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    try:
        data = request.get_json()
        db.add(data)
        return {"result": "added data successfuly!"}
    except:
        return {"reuslt": "Failed!"}
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    pass


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    pass


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    pass



if __name__ == '__main__':
    app.run(debug=True)