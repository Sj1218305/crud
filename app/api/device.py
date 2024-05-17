import json
from flask import jsonify, request
from app.api import api
import os

DATA_FILE = 'devices.json'

def load_devices():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_devices(devices):
    with open(DATA_FILE, 'w') as f:
        json.dump(devices, f)

@api.route('/devices', methods=['GET'])
def get_devices():
    devices = load_devices()
    return jsonify(devices)

@api.route('/devices', methods=['POST'])
def create_device():
    data = request.json
    devices = load_devices()
    new_device = {
        "id": len(devices) + 1,
        "name": data['name'],
        "status": data['status']
    }
    devices.append(new_device)
    save_devices(devices)
    return jsonify({'message': 'Device created successfully', 'device': new_device})

@api.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.json
    devices = load_devices()
    device = next((d for d in devices if d['id'] == device_id), None)
    if device is None:
        return jsonify({'message': 'Device not found'}), 404
    device['name'] = data['name']
    device['status'] = data['status']
    save_devices(devices)
    return jsonify({'message': 'Device updated successfully'})

@api.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    devices = load_devices()
    devices = [d for d in devices if d['id'] != device_id]
    save_devices(devices)
    return jsonify({'message': 'Device deleted successfully'})
