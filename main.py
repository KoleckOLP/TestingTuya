import time
from importlib import reload
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
from secret import productid, uuid, authkey
import DataFromESP32

#coloredlogs.install(level='DEBUG')

client = TuyaClient(productid=productid,
                    uuid=uuid,
                    authkey=authkey)

def on_connected():
    print('Connected.')

def on_qrcode(url):
    qrcode_generate(url)

def on_reset(data):
    print('Reset:', data)

# when there is a change in the Data Ponts this is called
def on_dps(dps):
    print('DataPoints:', dps)
    client.push_dps(dps)

client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

dps = {
    '101': True,  # Indoor Temperature
    '102': True,  # Indoor Humidity
    '103': True,  # Indoor Pressure
    '104': True   # Indoor Altitude
}

'''
dps = {'105': True}  # Outdoor Temperature
dps = {'106': True}  # Outdoor Humidity
dps = {'107': True}  # Outdoor Pressure
dps = {'108': True}  # Outdoor Altitude
'''

while True:
    reload(DataFromESP32)

    dps['101'] = DataFromESP32.in_temp
    dps['102'] = DataFromESP32.in_hum
    dps['103'] = DataFromESP32.in_press
    dps['104'] = DataFromESP32.in_alt

    '''
    dps['105'] = DataFromESP32.out_temp
    dps['106'] = DataFromESP32.out_hum
    dps['107'] = DataFromESP32.out_press
    dps['108'] = DataFromESP32.out_alt
    '''

    #print(dps)

    client.push_dps(dps)

    time.sleep(1)
