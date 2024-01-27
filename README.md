# TestingTuya
I would like to make my own tuya device but I can't find sdk documentation.

## how to make a working tuya project in python

1. register on https://iot.tuya.com/
2. create a procut and set it to Custom, Others, Wifi, Common Device
3. on the hardware development tab make request free licences, and download the .cvs file which will contain your uuid and authkey
4. on the function tab create your datapoints<br>
    what you need to do if you want decimal points you need to set scale to number of decimal poinst and keep pitch at 1
    and your range needs to be bigger by the amount of decimal points<br>
    for example the BME280 has temperature of -40 to 85 with 2 decimals, so your datapoint setting will be -4000 to 8000, pitch 1, scale 2<br>
    and the data you will be sending will be an integer and not a float so if you do have an float like 24.00 just multiply it by 100 to get 2400 and sent that to tuya<br>
5. once you have your datapoints go to Device integration tab, and change pannel to Studio Panel, and edit it to your liking.
6. make a new python script and install the tuya link sdk python https://github.com/tuya/tuyaos-link-sdk-python `pip install tuyalinksdk`
7. copy the full example they provide, it does absolutely nothing but it's a good base https://github.com/tuya/tuyaos-link-sdk-python/blob/development/examples/outlet.py
8. fill your product id, uuid, and authkey
9. to send data from python to tuya create a dictionary, I give them default value of True
```
dps = {
    '101': True,
    '102': True,
    '103': True,
    '104': True
}
```
than you can feed the data into the data points like this `dps['101'] = DataFromESP32.in_temp`<br>
and when you have the data in the dictionary you push it to tuya by using `client.push_dps(dps)`<br>
10. to receive data you use the fucntion they made for you in the example<br>
```
def on_dps(dps):
    print('DataPoints:', dps)
    client.push_dps(dps)
```
if you change something using the tuya app, it will be in the dps dictionary.

### - things you might need to know, after compiling and publishing your pannel with takes a while like 5-10 minutes, you need to wait yet another like 5 minutes for the pannel to load to your phone.

### - If you are changing datapoints you need to delete storrage.json delete the device from your phone and add it again.

### - just be patient over all everything takes a while before it starts working, like it may look like tuya is not getting the datapoints from you but it's just not synced with the cloud yet.

### - I'm sorry that this """tutorial""" is shitty but there is no documentation from tuya and I had to figure it out but it works so what the heck.

### ramble ramble tutorial bad.

if this helps noone it's atleast for me to remember how to do this crap