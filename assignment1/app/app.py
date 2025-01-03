from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# CRUD routes
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    item = Item(name=data['name'], description=data['description'])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200

@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict()), 200

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get_or_404(id)
    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify(item.to_dict()), 200

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)