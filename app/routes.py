from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_device')
def add_device():
    return render_template('add_device.html')

@app.route('/edit_device/<int:device_id>')
def edit_device(device_id):
    return render_template('edit_device.html', device_id=device_id)
