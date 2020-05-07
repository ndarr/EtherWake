from flask import Flask, request
import configparser
from wakeonlan import send_magic_packet
from flask_cors import CORS
from peewee import SqliteDatabase
from model.model import Device
from playhouse.shortcuts import model_to_dict
from jsonpickle import encode
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_all_devices():
    devices = list(Device.select().dicts())
    return json.dumps(devices,default=str)

@app.route('/wakeup/<device>')
def wake_up(device):
    device_mac = Device.select(Device.mac).where(Device.mac == device).get()
    if device_mac:
        send_magic_packet(device_mac)
        return "Success"
    else:
        return "Device not found"

@app.route('/device', methods=['POST'])
def add_device():
    body = request.json
    name = body['name']
    mac = body['mac']
    Device.create(name=name, mac=mac)
    return "Success"
    

if __name__ == '__main__':
    app.run()
