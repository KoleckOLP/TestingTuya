#!/usr/bin/env python
import time
from random import randint
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
from secret import productid, uuid, authkey

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

def on_dps(dps):  # when there is a change in the Data Ponts this is called
    print('DataPoints:', dps)
    client.push_dps(dps)

client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

while True:
    time.sleep(1)
    dps = {'101': True}
    dps['101'] = randint(0, 100)
    client.push_dps(dps)