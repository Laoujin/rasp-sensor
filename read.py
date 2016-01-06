import os
import glob
import time
import requests

# Example output: `cat w1_slave`
# 57 01 4b 46 7f ff 09 10 c7 : crc=c7 YES
# 57 01 4b 46 7f ff 09 10 c7 t=21437

# TODO:
# -> put in class, unit test it
# -> configuration in config file
# -> error handling for post
# -> backup on failure: add current time (GMT) and write to file

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

expressjsUrl = '192.168.1.24:8181'
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()

	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temperature = float(temp_string) / 1000.0
		return temperature

def post_temp(temperature):
	r = requests.post("http://" + expressjsUrl + '/api/temp', data={'@temp': temperature})
	return r.status_code, r.reason, r.text

# while True:
print(post_temp(read_temp()))
time.sleep(1)