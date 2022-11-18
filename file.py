import smbus
import time

address = 0x23
start = 0x01
stop = 0x00
reset = 0x07

bus = smbus.SMBus(1)

def lightRead():
	updatedAddress = bus.read_i2c_block_data(BH1750_sensor, address)
	value = lightConversion(updatedAddress)
	return value

def lightConversion(newAddress):
	conversion = ((newAddress[1] + (256 * newAddress[0]))/1.2)
	return conversion


while True:
    light_intensity = lightRead()
    print(light_intensity)
    
    print("Status:")
    if(light_intensity >= 500):
        print("Too bright")
    elif(light_intensity >= 200 and light_intensity < 500):
        print("Bright")
    elif(light_intensity >= 50 and light_intensity < 200):
        print("Tedium")
    elif(light_intensity > 20 and light_intensity < 50):
        print("Dark")
    elif(light_intensity < 20):
        print("Too dark")
    time.sleep(1)

