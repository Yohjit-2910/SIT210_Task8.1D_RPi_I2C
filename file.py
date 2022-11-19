import smbus		#important libraries.
import time

address = 0x23
start = 0x01		#addresses used by the I2C protocol
stop = 0x00
reset = 0x07

bus = smbus.SMBus(1)	# initializing the instance for the SMbus.

def lightRead():
	updatedAddress = bus.read_i2c_block_data(address, address)
	value = lightConversion(updatedAddress)		#function to get values of light intensity in float
	return value

def lightConversion(newAddress):
	conversion = ((newAddress[1] + (256 * newAddress[0]))/1.2)
	return conversion				# this fucntion will be used to convert the intensity values in understandable numbers


while True:
    light_intensity = lightRead()			#read the intensity of light.
    print(light_intensity)				# print intensity of light on shell
    
    if(light_intensity >= 2000):
        print("Status: Too bright")			
        print()
    elif(light_intensity >= 200 and light_intensity < 2000):
        print("Status: Bright")				# condition to print the intensity of light as Too Bright, Bright, Medium, Dark, Too Dark
        print()
    elif(light_intensity >= 50 and light_intensity < 200):
        print("Status: Medium")
        print()
    elif(light_intensity > 20 and light_intensity < 50):
        print("Status: Dark")
        print()
    elif(light_intensity <= 20):
        print("Status: Too dark")
        print()
    time.sleep(1)
