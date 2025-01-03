from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongodb:27017/')
db = client.treasurebook

@app.route('/node', methods=['POST'])
def add_node():
    data = request.get_json()
    node_type = data.get('type')  # 'Treasure', 'Location', 'Map'
    name = data.get('name')
    
    # Add the node to MongoDB based on its type
    node = {"type": node_type, "name": name}
    db.nodes.insert_one(node)
    
    return jsonify({"message": f"{node_type} added successfully!"}), 201

@app.route('/edge', methods=['POST'])
def add_edge():
    data = request.get_json()
    edge_type = data.get('type')  # 'Trail', 'Hidden-At', 'Leads-to'
    start_node = data.get('start')  # The starting node (e.g., "Forest of Secrets")
    end_node = data.get('end')     # The ending node (e.g., "Mystic Lake" or "Golden Crown")
    
    # Add the edge (relationship) to MongoDB
    edge = {"type": edge_type, "start": start_node, "end": end_node}
    db.edges.insert_one(edge)
    
    return jsonify({"message": f"{edge_type} relationship added successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
