from flask import Flask
import configparser
from wakeonlan import send_magic_packet
from json.encoder import JSONEncoder
from flask_cors import CORS


config = configparser.ConfigParser()

config.read('etherwake.cfg')
macs = config['CONFIG']['macs'].split(",")
macs = [mac.strip() for mac in macs]

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return JSONEncoder().encode(macs)

@app.route('/wakeup/<device>')
def wake_up(device):
    if device in macs:
        send_magic_packet(device)
        return "Success"
    else:
        return "Device not found"

@app.route('/wakeupall')
def wake_up_all():
    send_magic_packet(*macs)
    return "Success"


if __name__ == '__main__':
    app.run()
