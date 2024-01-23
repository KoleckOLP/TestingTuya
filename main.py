#!/usr/bin/env python
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

dps = {'101': True}

while True:
    reload(DataFromESP32)

    dps['101'] = DataFromESP32.temperature
    client.push_dps(dps)

    #print(dps)  # old debug output

    time.sleep(1)

'''
    dps = {'102': True}
    dps['102'] = humidity

    dps = {'103': True}
    dps['103'] = pressure

    dps = {'104': True}
    dps['104'] = altitude
'''


