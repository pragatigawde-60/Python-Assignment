import configparser
import json
from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Flask app
app = Flask(__name__)

# MongoDB setup
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "devops_config"
COLLECTION_NAME = "configurations"

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    # Test connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully.")
except ConnectionFailure:
    print("Failed to connect to MongoDB.")
    exit(1)

# Parse configuration file
def parse_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        result = {}
        for section in config.sections():
            result[section] = dict(config.items(section))
        return result
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return {}

# Save parsed data to MongoDB
def save_to_mongo(parsed_data):
    for section, data in parsed_data.items():
        # Upsert: update if exists, else insert
        collection.update_one(
            {"section": section},
            {"$set": {"data": data}},
            upsert=True
        )
    print("Configuration data saved to MongoDB successfully.")

# Flask endpoint to get configuration
@app.route('/config', methods=['GET'])
def get_config():
    configs = {}
    for doc in collection.find():
        configs[doc['section']] = doc['data']
    return jsonify(configs)

# Main execution
if __name__ == "__main__":
    config_file = "config.ini"
    parsed_data = parse_config(config_file)
    if parsed_data:
        save_to_mongo(parsed_data)
        print(json.dumps(parsed_data, indent=4))
    app.run(debug=True)
